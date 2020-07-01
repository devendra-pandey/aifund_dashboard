from flask import Flask, render_template, redirect, url_for, flash,request, current_app
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




# @app.route('/createprofile', methods=['GET', 'POST'])
@login_required
def create_profile():
    user_id = current_user.id
    model = Model.query.all() 
    stock = Stock.query.filter_by(is_active='1').all()
    
    if request.form:
        f = request.files['file_path']
        rd = request.form.get("report_date")
        vr = request.form.get("modelversion_id")

        pro_date = Profile.query.filter_by(report_date = rd).filter_by(modelversion_id = vr).filter_by(is_active = '1').all()
        for prof in pro_date:
            prof_date = prof.report_date
            prof_id = prof.id
            print(prof_id)

            item = Profile.query.get(prof_id)
            item.is_active = False
            db.session.add(item)
            db.session.commit()

            stock_profile = Stock.query.filter_by(profile_id = prof_id ).filter_by(is_active='1').all()
            for stock_pro in stock_profile:
                stock_id = stock_pro.id
                print(stock_id)

                stock_item = Stock.query.get(stock_id)
                stock_item.is_active = False
                db.session.add(stock_item)
                db.session.commit()

            

        print(type(f))
        # f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
        filename = str(int(round(time.time() * 1000)))+".csv"
        
        abs=os.path.join(current_app.config['UPLOAD_FOLDER'],filename)
        
        f.save(abs)
        # f.save(secure_filename(f.filename))
        
        profile = Profile(report_date=request.form.get("report_date"),modelversion_id=request.form.get("modelversion_id"),filename=f.filename)
        
        haeder_list = [
            'Code', 'BSE_Scrip_Name', 'instrument_token', 'model_decision',
            'stop_loss', 'stop_gain', 'trigger', 'Previous_Close',
            'Today_Open', 'Today_Close', 'delta_previous_today',
            'actual_delta', 'return_generated', 'Quantity',
            'Quantity_adjusted', 'total_return', 'transaction_value',
            'new_transaction_value', 'traditional_brokerage',
            'zerodha_brokerage', 'hybrid_brokerage',
            'total_return_after_traditional_brokerage',
            'total_return_after_zerodha_brokerage',
            'total_return_after_hybrid_brokerage'
        ]
        # profile1 = Profile.query.filter_by(file_path=f.filename).first()
        # abc = profile1.id
        csv1 = open(abs, "r")
        
        data = csv.DictReader(csv1)
        headers = data.fieldnames
        set_header = set(headers)
        set_header_list = set(haeder_list)
        if not set_header_list.issubset(set_header):
            flash('Please Check the Header Of the csv file')
            return redirect(url_for('create_profile'))
    
        
        db.session.add(profile)
        db.session.commit()
        print(profile.id)
        
        for row in data:
            code = row['Code']
            name = row['BSE_Scrip_Name']
            model_decision = row['model_decision']
            # exchange_token = row['exchange_token']
            instrument_token = row['instrument_token']
            stop_loss = row['stop_loss']
            stop_gain = row['stop_gain']
            triggered = row['trigger']
            previous_close = row['Previous_Close']
            today_open = row['Today_Open']
            today_close = row['Today_Close']
            delta_previous_today = row['delta_previous_today']
            actual_delta = row['actual_delta']
            return_generated = row['return_generated']
            quantity = row['Quantity']
            quantity_adjusted = row['Quantity_adjusted']
            total_return = row['total_return']
            transaction_value = row['transaction_value']
            new_transaction_value = row['new_transaction_value']
            traditional_brokerage = row['traditional_brokerage']
            zerodha_brokerage = row['zerodha_brokerage']
            hybrid_brokerage = row['hybrid_brokerage']
            tra_traditional_brokerage = row['total_return_after_traditional_brokerage']
            tra_zerodha_brokerage = row['total_return_after_zerodha_brokerage']
            tra_hybrid_brokerage = row['total_return_after_hybrid_brokerage']


            stock = Stock(
                    code=code,
                    name=name,
                    instrument_token=instrument_token,
                    model_decision=model_decision,
                    stop_loss=stop_loss,
                    stop_gain=stop_gain,
                    triggered=triggered,
                    previous_close=previous_close,
                    today_open=today_open,
                    today_close=today_close,
                    delta_previous_today=delta_previous_today,
                    actual_delta=actual_delta,
                    return_generated=return_generated,
                    quantity=quantity,
                    quantity_adjusted=quantity_adjusted,
                    total_return=total_return,
                    transaction_value=transaction_value,
                    new_transaction_value=new_transaction_value,
                    traditional_brokerage=traditional_brokerage,
                    zerodha_brokerage=zerodha_brokerage,
                    hybrid_brokerage=hybrid_brokerage,
                    tra_traditional_brokerage=tra_traditional_brokerage,
                    tra_zerodha_brokerage=tra_zerodha_brokerage,
                    tra_hybrid_brokerage=tra_hybrid_brokerage,
                    profile_id= profile.id)

            db.session.add(stock)
            db.session.commit()
        flash('Successfully Added',"success")
        return redirect(url_for('create_profile'))
    
    
    return render_template('create_profile.html', model=model, stock=stock)



