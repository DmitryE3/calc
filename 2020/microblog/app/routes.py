from app import app
from flask import render_template, flash, url_for, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.forms.forms import LoginForm
from werkzeug.urls import url_parse
from app import db
from app.forms.forms import RegistrationForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Diman'}
    posts = [{'author': {'username': 'Vladimir Lenin'}, 'body': 'Learn, Laern, Laern'},
             {'author': {'username': 'Aleksandr Pushkin'}, 'body': 'Evgeniy Inegin rulez'},
             {'author': {'username': 'Karl Marx'}, 'body': 'Working class not for us'}]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(password=form.password.data):
            flash('Invalid username or password. Please try again')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)  # Обработка логина пользователя
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='SignIn', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Congrats! You are now a registered, {form.username.data}')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post1'},
        {'author': user, 'body': 'Test post 666'}
    ]
    return render_template('user.html', user=user, posts=posts)
