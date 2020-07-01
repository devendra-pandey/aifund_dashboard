from flask import render_template, redirect, url_for,flash,request,session
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import InputRequired, Email, Length
from flask_login import login_required, login_user, logout_user,current_user
from models.user import User
from db import db
from forms.loginform import LoginForm
from forms.registrationform import RegisterForm
from sqlalchemy.exc import IntegrityError


def signup():
    
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,
                                                 method='sha256')

        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=hashed_password)
        user = request.form['username']
        email = request.form['email']
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Successfully Registered',"success")
        except IntegrityError:
            flash('Dublicate Entry',"danger")

    return render_template('signup.html', form=form)


def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, form.password.data):
                
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
            elif not user  :
                flash('Check the user name', "danger")
            else:
                flash('Worng Password',"danger")

        return render_template('login.html', form=form)


# @app.route('/logout')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('login'))