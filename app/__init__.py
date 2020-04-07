# Import flask and template operators
from flask import Flask, render_template,session

from flask_session import Session


from flask import app as app

import tempfile

from elasticsearch import Elasticsearch


# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy_searchable import SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import make_searchable

# Define the WSGI application object
app = Flask(__name__)




# Configurations
app.config.from_object('config')

app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None




# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


app.secret_key = 'super-secret-key'
Session(app)



# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_test.controllers import mod_test as test_module
from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_client.controllers import mod_client as client_module
from app.mod_quote.controllers import mod_quote as quote_module
from app.mod_product.controllers import mod_product as product_module
from app.mod_project.controllers import mod_project as project_module
from app.mod_config.controllers import mod_config as config_module
from app.mod_expense.controllers import mod_expense as expense_module

# Register blueprint(s)
app.register_blueprint(test_module)
app.register_blueprint(auth_module)
app.register_blueprint(client_module)
app.register_blueprint(quote_module)
app.register_blueprint(product_module)
app.register_blueprint(project_module)
app.register_blueprint(config_module)
app.register_blueprint(expense_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

