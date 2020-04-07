from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db
from passlib.hash import sha256_crypt
import json, jsonpickle

import time 
from datetime import datetime

from app.mod_expense.models import Expense,Tag

mod_expense = Blueprint('expense', __name__, url_prefix='/expense')


@mod_expense.route('/test', methods=['GET', 'POST'])
def landing():
    print("Got the hit")
    return render_template("mod_expense/bill-create.html")

@mod_expense.route('/bills/', methods=['GET', 'POST'])
def billsAll():
    print("Got the hit")
    return render_template("mod_expense/bill-list.html")


@mod_expense.route('/api/expense/create', methods=['POST'])
def api_createExpenseEntry():
    print("Got hit for expense head create api")
    request_json = request.json
    title = "TestExpense"
    meta = "TestMetaString"
    amount = 12
    headID = 1
    eh = Expense( title, meta,amount,headID)
    db.session.add(eh)
    db.session.commit()
    resp = jsonify(success=True)
    return resp
    
