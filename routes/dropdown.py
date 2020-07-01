from flask import Flask,jsonify, render_template, redirect, url_for, flash,request, current_app
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug import secure_filename
from datetime import datetime
import csv
import os
from models.model import Model
from models.modelversion import Modelversion
from models.profile import Profile
from models.stock import Stock
from db import db
import time


# @app.route('/dropdown')
@login_required
def dropdown(model_id):
    # model123 = request.GET("model_id")
    print(model_id)
    mv = Modelversion.query.filter_by(model_id=model_id).all()
    
    if not mv:
        return jsonify({'message': 'model does not exist'})
    else:
        list_of_version = []
        for id in mv:
            version_data = {}
            version_data['id']= id.id
            version_data['version'] = id.version
            list_of_version.append(version_data)

    return jsonify({'list_of_version': list_of_version})

