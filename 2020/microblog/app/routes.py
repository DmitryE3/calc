from app import app
from flask import render_template, flash, url_for, redirect
from app.forms.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Diman'}
    posts = [{'author': {'username': 'Vladimir Lenin'}, 'body': 'Learn, Laern, Laern'},
             {'author': {'username': 'Aleksandr Pushkin'}, 'body': 'Evgeniy Inegin rulez'},
             {'author': {'username': 'Karl Marx'}, 'body': 'Working class not for us'}]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='SignIn', form=form)