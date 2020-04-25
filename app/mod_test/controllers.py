from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db


# Import module models (i.e. User)
#from app.mod_test.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth

mod_test = Blueprint('test', __name__, url_prefix='/test')


"""et the route and accepted methods

"""
@mod_test.route('/test1/', methods=['GET', 'POST'])
def signin():
    print("Got the hit")
    return render_template("mod_test/test.html")

@mod_test.route('/spreadsheet/', methods=['GET', 'POST'])
def launchSpreadsheet():
    print("Got the hit")
    return render_template("mod_test/spreadsheet.html")