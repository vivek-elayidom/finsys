from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for,jsonify

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

import time
from sqlalchemy import literal
import json

import jsonpickle


# Import module models (i.e. User)
#from app.mod_client.models import Client
#from app.mod_client.models import Contact

#from app.mod_client.sample_data import sampleClientList

# Define the blueprint: 'auth', set its url prefix: app.url/auth

mod_client = Blueprint('client', __name__, url_prefix='/client')


"""et the route and accepted methods

@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html", form=form)







@mod_client.route('/create', methods=['GET', 'POST'])
def addClient():
    print("Got the hit")
    id = int(time.time())
    return render_template("mod_client/AddClients.html", id=id)


@mod_client.route('/contact/create', methods=['GET', 'POST'])
def addContact():
    print("Got the hit")
    id = int(time.time())
    return render_template("mod_client/AddContact.html", id=id)

@mod_client.route('/detail/<int:id>/', methods=['GET','POST'])
def detailPage(id):
    print("Got hit on the detailPage")
    client = Client.query.get(id)
    return render_template("mod_client/ClientDetail.html", client=client)

@mod_client.route('/contact-detail/<int:id>/', methods=['GET','POST'])
def contact_Detail(id):
    print("Got hit on the detailPage")
    contact = Contact.query.get(id)
    return render_template("mod_client/ContactDetail.html", client=contact)


@mod_client.route('/browse/<int:pnum>/', methods=['GET','POST'])
def browseClients(pnum):
    if(request.method == "GET"):
        print("Got the hit after redirection -its a get request")
    if(session.get('client_searchSetStatus')):
        print("Session is search set, return search result")
        print(session['clientsearch_startDate'], session['clientsearch_query'])
    print("proceeding",request)
    record_query = Client.query.paginate(pnum, 10, False)
    total = record_query.total
    print(record_query, "total")
    clients = Client.query.all()
    totalpages = (len(clients)//10 +1)
    print("totalpages", totalpages)
    return render_template("mod_client/BrowseClients.html", clientList= record_query.items,len = len(record_query.items),pnum =pnum,totalpages=totalpages)

@mod_client.route('/browse-contact/<int:pnum>/', methods=['GET','POST'])
def browseContacts(pnum):
    if(request.method == "GET"):
        print("Got the hit after redirection -its a get request")
    if(session.get('client_searchSetStatus')):
        print("Session is search set, return search result")
        print(session['clientsearch_startDate'], session['clientsearch_query'])
    print("proceeding",request)
    record_query = Contact.query.paginate(pnum, 10, False)
    total = record_query.total
    print(record_query, "total")
    contacts = Contact.query.all()
    totalpages = (len(contacts)//10 +1)
    print("totalpages", totalpages)
    return render_template("mod_client/BrowseContacts.html", contactList= record_query.items,len = len(record_query.items),pnum =pnum,totalpages=totalpages)


def obj_dict(obj):
    return obj.__dict__

class ClientURL:
  def __init__(self, name, id,country):
    self.name = name
    self.id = id
    self.country = country

@mod_client.route('/api/v1.0/search/', methods=['GET'])
def getSearch():
    searchTerm = request.args.get('q')
    print("searchTerm",searchTerm)
    query, total = Client.search(searchTerm, 1, 5)
    print(query.all())
    resp = []
    for item in query.all():
        ret = ClientURL(item.org_name,item.id,item.country)
        #ret = item.org_name
        print(ret,"searchResultitem")
        resp.append(ret)
    return jsonpickle.encode(resp,unpicklable=False)

@mod_client.route('/api/v1.0/create', methods=['POST'])
def create_task():
    #print(request.get_data())
    request_json     = request.json
    print("Got the hit",request_json)
    #session.get('logged_in') == True:  {'name': 'sdss', 'city': 
    #'sd', 'vat': 'sdsd', 'country': 'India', 'clientID': ' 1575541447', 
    #'state': 'sd', 'address2': 'sd', 'address1': 'sd', 'site': 'sdsd.ci'}
    # def __init__(self, name, website, phoneNumber,address1,address2,city,state,country):
    name = request_json['name']
    city = request_json['city']
    vat = request_json['vat']
    country = request_json['country']
    clientID = request_json['clientID']
    state = request_json['state']
    address1 = request_json['address1']
    address2 = request_json['address2']
    site = request_json['site']
    clientID = request_json['clientID']
    phoneNumber = 123456
    client = Client(org_name = name, website=site,phoneNumber= phoneNumber, address1=address1, address2=address2,city=city,state=state,country=country,clientID=clientID)
    db.session.add(client)
    db.session.commit()
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@mod_client.route('/api/v1.0/setSearch', methods=['POST'])
def set_search():
    #print(request.get_data())
    request_json     = request.json
    print("Got the hit",request_json)
    resp = jsonify(success=True)
    resp.status_code = 200
    #print(sess)
    session['client_searchSetStatus'] = 1
    session['clientsearch_startDate'] = request_json['start']
    session['clientsearch_endDate'] = request_json['end']
    session['clientsearch_query'] = request_json['query']
    print(session['clientsearch_query'])
    #return redirect(url_for('client.list', pnum = 2),code=302)
    #return redirect(url_for('client.test'),code=302)
    resp = jsonify(success=True)
    return resp

@mod_client.route('/api/v1.0/addcontact', methods=['POST'])
def create_contact():
    #print(request.get_data())
    #{'position': 'sdsd', 'companyID': 13, 'linkedInURL': 'sds.com', 'company': 'MES logistics', 
    #'contactID': ' 1575758286', 'email': 'sd@sd.com', 'name': 'sdsd'}
    request_json     = request.json
    position = request_json['position']
    companyID = request_json['companyID']
    linkedInURL = request_json['linkedInURL']
    company = request_json['company']
    contactID = request_json['contactID']
    email = request_json['email']
    name = request_json['name']
    # def __init__(self, name, linkedIN, email,phoneNumber,orgID,orgName,position,contactID):
    contact = Contact(name = name, linkedIN=linkedInURL,email= email,phoneNumber= 12345678, orgID=companyID, orgName=company, position=position,contactID=contactID )
    db.session.add(contact)
    db.session.commit()
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

"""