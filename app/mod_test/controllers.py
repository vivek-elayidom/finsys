from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash


# Import the database object from the main app module
from app import db
import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("localhost", 27017)
db = client.test

mycol = db["estimates"]


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


@mod_test.route('/tablePost', methods=['POST'])
def api_createTablePost():
    print("Got hit for expense head create api")
    request_json = request.json
    #print(request_json)
    returnID = ""
    mycol = db["estimates"]
    if (request_json['mongoID']):
        print("Update starting")
        thing = mycol.find_one({'_id': ObjectId(request_json['mongoID']) })
        print(thing)
        mydict = { "name": request_json['name'], "html": request_json['html'],"data":request_json['celldata'],"sectiondata":request_json['sectiondata'],"title":request_json['title'] }
        mycol.replace_one({'_id': ObjectId(request_json['mongoID']) }, mydict)
        print(thing)
        returnID = request_json['mongoID']
    else:
        mydict = { "name": request_json['name'], "html": request_json['html'] ,"data":request_json['celldata'],"sectiondata":request_json['sectiondata'],"title":request_json['title'] }
        x = mycol.insert_one(mydict)
        returnID = str(x.inserted_id)
    resp = jsonify(success=True,id=returnID)
    return resp

@mod_test.route('/spreadsheet/<string:id>',methods=['GET'])
def api_getTableData(id):
    print("Got hit for table from Mongo API")
    resp = jsonify(success=True)
    myquery = { "_id": id }
    #mydoc = mycol.find_one()
    thing = mycol.find_one({'_id': ObjectId(id) })
    #for x in mydoc:
    #    print(x)
    return render_template("mod_test/spreadsheet.html",html=thing)

@mod_test.route('api/estimate/<string:id>',methods=['GET'])
def api_getTableDataAPI(id):
    print("Got hit on getTable Data API")
    #myquery = { "_id": id }
    thing = mycol.find_one({'_id': ObjectId(id) })
    resp = jsonify(success=True,html=thing['html'],celldata=thing['data'],sectiondata=thing['sectiondata'],title=thing['title'])
    return resp
