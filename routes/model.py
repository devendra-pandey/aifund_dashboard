from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from models.model import Model
from db import db
from sqlalchemy.exc import IntegrityError


# @app.route('/createmodel', methods=['GET', 'POST'])
@login_required
def create_model():
    user_id = current_user.id
    if request.form:

        model_name = request.form.get("name", "").strip()
        model_description = request.form.get("description", "").strip()

        if len(model_name) == 0 :
            flash('Model name should not be empty', "danger")
            return render_template('create_model.html')
        elif len(model_description) ==0:
            flash('Description should not be empty', "danger")
            return render_template('create_model.html')

        models = Model.query.filter_by(name=model_name).all()
        

        if len(models) > 0:
            flash('Model Already Exists', "danger")
            return render_template('create_model.html')

        model = Model(name=model_name,
                      description=request.form.get("description"),
                      user_id=user_id)
        try:
            db.session.add(model)
            db.session.commit()
            flash('Successfully Added', 'success')
        except IntegrityError:
            flash('Model Already Exists', "danger")

    return render_template('create_model.html')
