from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

# Import the database object from the main app module
from app import db
from passlib.hash import sha256_crypt
import json, jsonpickle
from app import app
import time 
from datetime import datetime
import os
from app.mod_expense.models import Expense,Tag
from app.mod_config.models import Vendor

mod_expense = Blueprint('expense', __name__, url_prefix='/expense')


@mod_expense.route('/test', methods=['GET', 'POST'])
def landing():
    print("Got the hit")
    return render_template("mod_expense/bill-create.html")

@mod_expense.route('/bills/', methods=['GET', 'POST'])
def billsAll():
    print("Got the hit")
    return render_template("mod_expense/bill-list.html")


@mod_expense.route('/api/createExpense', methods=['POST'])
def api_createExpenseEntry():
    print("Got hit for expense head create api")
    request_json = request.json
#    def __init__(self, title, meta,amount,headID,toEntityType,entityID,currency,t_date,r_date,status):
    title = request_json['title']
    meta = request_json['meta']
    amount = request_json['amount']
    headID = request_json['headID']
    toEntityType = request_json['toEntityType']
    entityID = request_json['entityID']
    currency = request_json['currency']
    t_date = request_json['t_date']
    r_date = request_json['r_date']
    status = request_json['status']
    eh = Expense( title, meta,amount,headID,toEntityType,entityID,currency,t_date,r_date,status)
    db.session.add(eh)
    db.session.commit()
    resp = jsonify(success=True)
    return resp
    
@mod_expense.route('/api/editExpense', methods=['POST'])
def api_editExpense():
    exp = db.session.query(Expense).get(request.json['id'])
    exp.title = request.json['title']
    exp.meta = request.json['meta']
    exp.amount = request.json['amount']
    exp.headID = request.json['headID']
    exp.toEntityType = request.json['toEntityType']
    exp.entityID = request.json['entityID']
    exp.currency = request.json['currency']
    exp.t_date = request.json['t_date']
    exp.r_date = request.json['r_date']
    exp.status = request.json['status']
    db.session.add(exp)
    db.session.commit()
    resp = jsonify(success=True)
    return resp

@mod_expense.route('/api/getAllExpenses', methods=['GET'])
def api_getAllExpenses():
    print("Got hit for allExpenses  API")
    records = db.session.query(Expense).all()
    d = []
    for item in records:
        k = []
        k.append(item.title)
        k.append(item.id)
        k.append(item.amount)
        k.append(item.currency)
        k.append(item.toEntityType)
        #ret = item.org_name
        d.append(k)
    resp = jsonify(data=d)
    return resp

@mod_expense.route('/api/newAllExpenses', methods=['GET'])
def api_newAllExpenses():
    print("Got hit for allExpenses  API")
    records = db.session.query(Expense).all()
    d = []
    for item in records:
        k = {}
        k['title'] = item.title
        k['id'] = item.id
        k['amount'] = item.amount
        k['display_amount'] = str(item.amount) + ' ' + item.currency
        k['currency'] = item.currency
        k['date'] = str(item.transaction_date.date())
        d.append(k)
    resp = jsonify(data=d)
    return resp



ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@mod_expense.route('/api/upload', methods=['POST'])
def api_fileUpload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if not os.path.exists(app.config['UPLOAD_FOLDER'] + '/another'):
                os.makedirs(app.config['UPLOAD_FOLDER'] + '/another')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/another', filename))
            print('getcwd:      ', os.getcwd())
            resp = jsonify(success=True)
            return resp

@mod_expense.route('/api/getByID/<int:id>',methods=['GET'])
def api_expenseByID(id):
    #id = request.json['id']
    expense = Expense.query.get(id)
    print(expense)
    title = expense.title
    meta = expense.meta
    amount = expense.amount
    headID = expense.headID
    vendorID = expense.entityID
    currency = expense.currency
    t_date = expense.transaction_date
    status = expense.status
    vendor = Vendor.query.get(vendorID)
    vendorName = vendor.name
    resp = jsonify(success=True,title=title,remarks=meta, amount=amount,category=headID,vendorID=vendorID,vendorName=vendorName, currency=currency,t_date=t_date,status=status)
    return resp