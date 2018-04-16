from flask_blog import app
from flask import render_template, redirect, url_for, session, request
from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required
import bcrypt


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():

        author = Author.query.filter_by(
            username=form.username.data
        ).first()
        if author:
            # print('count?')
            # author = authors[0]
            # print(author)
            if bcrypt.hashpw(form.password.data.encode('utf8'), author.password.encode()) \
                    == author.password.encode():
                # print('TRUE')
                session['username'] = form.username.data
                session['is_author'] = author.is_author
                if 'next' in session:
                    nexto = session.get('next')
                    session.pop('next')
                    return redirect(nexto)
                else:
                    return redirect(url_for('login_success'))
            else:
                # print('false')
                error = 'incorrect username/passwd'
        else:
            error = 'incorrect username/passwd'

    return render_template('author/login.html', form=form, error=error)
    
    
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)
    

@app.route('/login_success')
@login_required
def login_success():
    return 'logged in'


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))


