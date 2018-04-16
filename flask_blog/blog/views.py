from flask_blog import app
from flask import render_template, redirect, flash, url_for, session, abort
from blog.form import SetupForm, PostForm
from flask_blog import db
from author.models import Author
from blog.models import Blog
from author.decorators import login_required, author_required
import bcrypt


@app.route('/')
@app.route('/index')
def index():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))

    return 'hi'
    

@app.route('/admin')
@author_required
def admin():
    if session.get('is_author'):
        return render_template('blog/admin.html')
    else:
        abort(403)


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    error = ''
    form = SetupForm()
    if form.validate_on_submit():

        salt = bcrypt.gensalt()
        hashed_pwd = bcrypt.hashpw(form.password.data.encode('utf-8'), salt)

        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_pwd,
            True
        )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(
                form.name.data,
                author.id
            )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = 'err. creatin user'

        if author.id and blog.id:
            db.session.commit()
        else:
            db.session.rollback()
            error = 'err.creatin blog'

        flash('blog created')
        redirect(url_for('admin'))

    return render_template('blog/setup.html', form=form, error=error)


@app.route('/post', methods=['POST', 'GET'])
@author_required
def post():
    form = PostForm()
    return render_template('blog/post.html', form=form)


@app.route('/article')
def article():
    return render_template('blog/article.html')
