from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for,jsonify

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

import time
from sqlalchemy import literal
import json

import jsonpickle


mod_project = Blueprint('project', __name__, url_prefix='/project')


@mod_project.route('/create/', methods=['GET', 'POST'])
def addQuote():
    print("Got the hit")
    return render_template("mod_project/AddProject.html")