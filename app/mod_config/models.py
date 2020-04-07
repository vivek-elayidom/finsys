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


class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class User(Base,SearchableMixin):
    __tablename__ = 'user'
    __searchable__ = ['username']
    # User Name
    username    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    password_hash    = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128), nullable=False)
    roleId = db.Column(db.Integer, nullable=False)
    phonenum = db.Column(db.String(128), nullable = True)
    departmentID = db.Column(db.Integer, nullable=True)


    # New instance instantiation procedure
    def __init__(self, username, password_hash, email, roleId,phonenum,departmentID):

        self.username     = username
        self.email = email
        self.roleId = roleId
        self.password_hash = password_hash
        self.phonenum = phonenum
        self.departmentID = departmentID


    def __repr__(self):
        return '<User %r>' % (self.username)

class Role(Base,SearchableMixin):
    __tablename__ = 'role'
    __searchable__ = ['name']
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    description    = db.Column(db.String(128),  nullable=False)


    # New instance instantiation procedure
    def __init__(self, name, description):

        self.name     = name
        self.description = description



class Department(Base,SearchableMixin):
    __tablename__ = 'department'
    __searchable__ = ['name']
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    description    = db.Column(db.String(128),  nullable=False)


    # New instance instantiation procedure
    def __init__(self, name, description):

        self.name     = name
        self.description = description

    def __repr__(self):
        return '<Department %r>' % (self.name)

class BankAccount(Base,SearchableMixin):
    __tablename__ = 'bank-account'
    __searchable__ = ['ac_name','bank_name']
    # User Name
    # OwnerType = 1 - mDrift Account, 2 - Customer Account, 3 - Vendor Account , 4 - Partner/Subsidiary Account
    ac_number = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    ac_name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    ifsc    = db.Column(db.String(128),  nullable=False)
    swift    = db.Column(db.String(128),  nullable=True)
    iban    = db.Column(db.String(128),  nullable=True)
    bank_name    = db.Column(db.String(128),  nullable=False) 
    branch_name    = db.Column(db.String(128),  nullable=False)
    owner_type = db.Column(db.Integer,  nullable=False)# Identification Data: email & password
    ownerID = db.Column(db.Integer, nullable=False)
    # New instance instantiation procedure
    def __init__(self, ac_name, ac_number,ifsc, swift,iban,bank_name,branch_name,owner_type,ownerID):

        self.ac_number     = ac_number
        self.ac_name = ac_name
        self.ifsc = ifsc
        self.swift = swift
        self.iban = iban
        self.bank_name= bank_name
        self.branch_name = branch_name
        self.owner_type = owner_type
        self.ownerID = ownerID

    def __repr__(self):
        return '<Department %r>' % (self.name)


class ExpenseHead(Base,SearchableMixin):
    __tablename__ = 'expenseheads'
    __searchable__ = ['name']
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    description    = db.Column(db.String(128),  nullable=False)


    # New instance instantiation procedure
    def __init__(self, name, description):

        self.name     = name
        self.description = description

    def __repr__(self):
        return '<ExpenseHead %r>' % (self.name)

class SalesEntity(Base,SearchableMixin):
    __tablename__ = 'salesentity'
    __searchable__ = ['name']
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    description    = db.Column(db.String(128),  nullable=False)
    uom    = db.Column(db.String(128),  nullable=False)
    currency = db.Column(db.String(128),  nullable=False)
    unitprice = db.Column(db.Integer , nullable=False)
    unit_type = db.Column(db.Integer, nullable=False)


    # New instance instantiation procedure
    def __init__(self, name, description,uom,currency,unitprice,unit_type):

        self.name     = name
        self.description = description
        self.uom = uom
        self.currency = currency
        self.unitprice = unitprice
        self.unit_type = unit_type


    def __repr__(self):
        return '<SalesEntity %r>' % (self.name)


class Project(Base):
    __tablename__ = 'project'
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    description    = db.Column(db.String(128),  nullable=False)
    account = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    finalQuote = db.Column(db.Integer, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, description,account,contact,finalQuote):

        self.name     = name
        self.description = description
        self.account = account
        self.contact = contact
        self.finalQuote = finalQuote


    def __repr__(self):
        return '<Project %r>' % (self.name)

class Employee(Base,SearchableMixin):
    __tablename__ = 'employee'
    __searchable__ = ['name']
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    employeeID    = db.Column(db.String(128),  nullable=False)
    departmentID = db.Column(db.Integer, nullable=False)
    dateofjoining = db.Column(db.DateTime, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    # New instance instantiation procedure
    def __init__(self, name, employeeID,departmentID,dateofjoining,userID):

        self.name     = name
        self.employeeID = employeeID
        self.departmentID = departmentID
        self.dateofjoining = dateofjoining
        self.userID = userID


    def __repr__(self):
        return '<Employee %r>' % (self.name)

class Company(Base,SearchableMixin):
    __tablename__ = 'company'
    __searchable__ = ['name']
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    country    = db.Column(db.String(128),  nullable=False)
    state = db.Column(db.String(128),  nullable=False)
    city = db.Column(db.String(128),  nullable=False)
    street1 = db.Column(db.String(128),  nullable=False)
    street2 = db.Column(db.String(128),  nullable=False)
    pin = db.Column(db.String(128),  nullable=False)
    company_type = db.Column(db.Integer,  nullable=False)
    # 1- Customer, 2 - Partner , 3 - Vendor
    
    # New instance instantiation procedure
    def __init__(self, name, country,state,city,street1,street2,pin,company_type):

        self.name     = name
        self.country = country
        self.state = state
        self.city = city
        self.street1 = street1
        self.street2 = street2
        self.pin = street2
        self.company_type = company_type


    def __repr__(self):
        return '<Company %r>' % (self.name)

class Vendor(Base,SearchableMixin):
    __tablename__ = 'vendor'
    __searchable__ = ['name']
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    country    = db.Column(db.String(128),  nullable=False)
    state = db.Column(db.String(128),  nullable=False)
    city = db.Column(db.String(128),  nullable=False)
    street1 = db.Column(db.String(128),  nullable=False)
    street2 = db.Column(db.String(128),  nullable=False)
    pin = db.Column(db.String(128),  nullable=False)
    company_type = db.Column(db.String(128),  nullable=False)
    vendorID = db.Column(db.String(128), nullable=False)
    beneficiary = db.Column(db.String(128), nullable=False)

    # 1- Customer, 2 - Partner , 3 - Vendor
    
    # New instance instantiation procedure
    def __init__(self, name, country,state,city,street1,street2,pin,company_type,vendorID,beneficiary):

        self.name     = name
        self.country = country
        self.state = state
        self.city = city
        self.street1 = street1
        self.street2 = street2
        self.pin = street2
        self.company_type = company_type
        self.vendorID = vendorID
        self.beneficiary = beneficiary
        


    def __repr__(self):
        return '<Company %r>' % (self.name)

