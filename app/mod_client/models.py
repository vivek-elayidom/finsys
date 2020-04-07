from app import db
from datetime import datetime
import random 
import string
import time

from app import app
from flask_sqlalchemy import SQLAlchemy, BaseQuery


  
# defining function for random 
# string id with parameter

from search import add_to_index, remove_from_index, query_index
'''
class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)


def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size)) 



# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class Client(Base,SearchableMixin):
    __tablename__ = 'client'
    __searchable__ = ['org_name']
    # User Name
    org_name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    website    = db.Column(db.String(128),  nullable=False)
    clientID  = db.Column(db.String(128), nullable=False,unique=True)
    phoneNumber = db.Column(db.String(128), nullable=False)
    address1 = db.Column(db.String(128), nullable=False)
    address2 = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=False)


    # New instance instantiation procedure
    def __init__(self, org_name, website, phoneNumber,address1,address2,city,state,country,clientID):

        self.org_name     = org_name
        self.website    = website
        self.clientID = str(int(time.time()))
        self.phoneNumber = phoneNumber
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.country = country

        

    def __repr__(self):
        return '<Client %r>' % (self.org_name)

class Contact(Base,SearchableMixin):
    __tablename__ = 'contact'
    __searchable__ = ['name','organisationName']
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    linkedIN    = db.Column(db.String(128),  nullable=False)
    organisationID  = db.Column(db.Integer , nullable=False)
    organisationName = db.Column(db.String(128), nullable=False)
    contactID = db.Column(db.String(128), nullable=False, unique=True)
    phoneNumber = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    position = db.Column(db.String(128), nullable=False)


    # New instance instantiation procedure
    def __init__(self, name, linkedIN, email,phoneNumber,orgID,orgName,position,contactID):

        self.name   = name
        self.linkedIN    = linkedIN
        self.organisationID = orgID
        self.organisationName = orgName
        self.contactID = contactID
        self.phoneNumber = phoneNumber
        self.email = email
        self.position = position

        

    def __repr__(self):
        return '<Client %r>' % (self.name)


db.create_all()
'''