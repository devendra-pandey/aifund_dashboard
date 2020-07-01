from flask import Flask, render_template, redirect, url_for, flash,request
from flask_bootstrap import Bootstrap
import os
import os.path
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from models.model import Model
from models.modelversion import Modelversion
from db import db



# @app.route('/createmv', methods=['GET', 'POST'])
@login_required
def create_mv():
    model = Model.query.all()
    if request.form:
        model_id = request.form.get("model")
        version_id = request.form.get("version")
        model_mv = Modelversion(model_id=request.form.get("model"),version=request.form.get("version"))
        model_v = Modelversion.query.filter_by(model_id=model_id).filter_by(version=version_id).all()
        if model_v:
            flash('Version Already exists for the model',"danger")
        else:
            db.session.add(model_mv)
            db.session.commit()
            flash('Successfully Added',"success")
        

    return render_template('create_mv.html' , model = model)