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
#from app.mod_config.models import Vendor,ExpenseHead

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/dash')

@mod_dashboard.route('/test', methods=['GET', 'POST'])
def landing():
    print("Got the hit")
    return render_template("mod_dashboard/test.html")