
from app import db
from datetime import datetime
import random 
import string
import time

from app import app
from flask_sqlalchemy import SQLAlchemy, BaseQuery


from app.mod_config.models import SearchableMixin

from search import add_to_index, remove_from_index, query_index
"""
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

    """

def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size)) 


class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Expense(Base,SearchableMixin):
    __tablename__ = 'expense'
    __searchable__ = ['title']
    # User Name
    title    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    meta    = db.Column(db.String(250),  nullable=False)
    amount = db.Column(db.Float, nullable=False)
    headID = db.Column(db.Integer,nullable=False)
    toEntityType = db.Column(db.String(128), nullable=False)
    entityID = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String(128), nullable=False)
    transaction_date = db.Column(db.DateTime,nullable=False)
    requested_date = db.Column(db.DateTime,nullable=False)
    status = db.Column(db.String(128), nullable=False)


    # New instance instantiation procedure
    def __init__(self, title, meta,amount,headID,toEntityType,entityID,currency,t_date,r_date,status):

        self.title     = title
        self.meta = meta
        self.amount = amount
        self.headID = headID
        self.toEntityType = toEntityType
        self.entityID = entityID
        self.currency = currency
        self.transaction_date = t_date
        self.requested_date = r_date
        self.status = status

class Tag(Base,SearchableMixin):
    __tablename__ = 'tag'
    __searchable__ = ['name']
    # User Name
    name    = db.Column(db.String(128),  nullable=False)# Identification Data: email & password
    description    = db.Column(db.String(250),  nullable=False)



    # New instance instantiation procedure
    def __init__(self, name, description):
        self.name     = name
        self.description = description

