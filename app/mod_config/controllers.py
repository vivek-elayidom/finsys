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

# Import module models (i.e. User)
from app.mod_config.models import User,Role,BankAccount,ExpenseHead,SalesEntity,Project,Employee,Department,Company,Vendor

# Define the blueprint: 'auth', set its url prefix: app.url/auth

mod_config = Blueprint('config', __name__, url_prefix='/configure')


def checklogin(session):
    if(session['logged_in'] == "trud"):
        return
    else:
        print("Not logged in")
        return redirect('/auth/test1')

@mod_config.route('/main', methods=['GET', 'POST'])
def landing():
    print("Got the hit")
    return render_template("mod_config/main.html")

@mod_config.route('/test', methods=['GET', 'POST'])
def test():
    print("Got the hit")
    return render_template("mod_config/starter.html")

@mod_config.route('/company/create', methods=['GET', 'POST'])
def companyCreate():
    print("Got the hit")
    return render_template("mod_config/company-create.html")

@mod_config.route('/vendor/create', methods=['GET', 'POST'])
def vendorCreate():
    print("Got the hit")
    return render_template("mod_config/vendor-create.html")

@mod_config.route('/bank-customer/create', methods=['GET', 'POST'])
def bankCustomerCreate():
    print("Got the hit")
    return render_template("mod_config/bank-customer-create.html")

@mod_config.route('/bank-vendor/create', methods=['GET', 'POST'])
def bankVendorCreate():
    print("Got the hit")
    return render_template("mod_config/bank-vendor-create.html")

@mod_config.route('/bank-employee/create', methods=['GET', 'POST'])
def bankEmployeeCreate():
    print("Got the hit")
    return render_template("mod_config/bank-employee-create.html")


@mod_config.route('/bank-mdrift/create', methods=['GET', 'POST'])
def bankMdriftCreate():
    print("Got the hit")
    return render_template("mod_config/bank-mdrift-create.html")

@mod_config.route('/employee/create', methods=['GET', 'POST'])
def empCreate():
    print("Got the hit")
    ts = time.time()
    empID = "EMP" +str(int(ts))
    departments = Department.query.all()
    roles = Role.query.all()
    return render_template("mod_config/employee-create.html",empID =empID,departments=departments ,roles = roles)

@mod_config.route('/expense-head/create', methods=['GET', 'POST'])
def expHeadCreate():
    print("Got the hit")
    return render_template("mod_config/expense-head-create.html")


@mod_config.route('/company/edit/<int:pnum>/', methods=['GET','POST'])
def companyEdit(pnum):
    print("Got the hit")
    id = pnum
    company = db.session.query(Company).get(id)
    companyID = company.id
    return render_template("mod_config/company-edit.html",company= company)

@mod_config.route('/vendor/edit/<int:pnum>/', methods=['GET','POST'])
def vendorEdit(pnum):
    print("Got the hit")
    id = pnum
    company = db.session.query(Vendor).get(id)
    return render_template("mod_config/vendor-edit.html",vendor= company)


@mod_config.route('/employee/edit/<int:pnum>/', methods=['GET','POST'])
def empEdit(pnum):
    print("Got the hit")
    id = pnum
    usr = db.session.query(User).get(id)
    userID = usr.id
    print(userID)
    emp = db.session.query(Employee).filter_by(userID = userID).first()
    departments = Department.query.all()
    roles = Role.query.all()
    print(emp)
    #print(usr)
    return render_template("mod_config/employee-edit.html",user= usr,employee = emp,departments=departments,roles=roles)


@mod_config.route('/role/create', methods=['GET', 'POST'])
def roleCreate():
    print("Got the hit")
    return render_template("mod_config/role-create.html")

@mod_config.route('/service/create', methods=['GET', 'POST'])
def serviceCreate():
    print("Got the hit")
    return render_template("mod_config/service-create.html")

@mod_config.route('/product/create', methods=['GET', 'POST'])
def productCreate():
    print("Got the hit")
    return render_template("mod_config/product-create.html")



# List Views

@mod_config.route('/user/list', methods=['GET'])
def userList():
    print("Got the hit for userlist")
    return render_template("mod_config/user-list.html")

@mod_config.route('/customer/list', methods=['GET'])
def customerList():
    print("Got the hit for userlist")
    return render_template("mod_config/company-list.html")

@mod_config.route('/bank-customer/list', methods=['GET'])
def bankCustomerList():
    print("Got the hit for bankCustomerList")
    return render_template("mod_config/bank-customer-list.html")

@mod_config.route('/bank-vendor/list', methods=['GET'])
def bankVendorList():
    print("Got the hit for bankVendorList")
    return render_template("mod_config/bank-vendor-list.html")

@mod_config.route('/bank-employee/list', methods=['GET'])
def bankEmployeeList():
    print("Got the hit for bankEmployeeList")
    return render_template("mod_config/bank-employee-list.html")

@mod_config.route('/vendor/list', methods=['GET'])
def vendorList():
    print("Got the hit for bankEmployeeList")
    return render_template("mod_config/vendor-list.html")

@mod_config.route('/bank-mdrift/list', methods=['GET'])
def bankmDriftList():
    print("Got the hit for bankMdriftList")
    return render_template("mod_config/bank-mdrift-list.html")
# POST and Create API for Config Model

@mod_config.route('/api/user/create', methods=['POST'])
def api_userCreate():
    print("Got the hit for createuserAPI")
    request_json = request.json
    username = request_json['username']
    hash_password = sha256_crypt.hash(request_json['password'])
    roleID = request_json['roleID']
    email = request_json['email']
    user = User(username,hash_password,email,roleID,"12232332",2)
    db.session.add(user)
    db.session.commit()
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@mod_config.route('/api/customer/create', methods=['POST'])
def api_createCustomer():
    print("Got the hit for createCustomer")
    #(self, name, country,state,city,street1,street2,pin,company_type):
    request_json = request.json
    name = request_json['name']
    country = request_json['country']
    state = request_json['state']
    city = request_json['city']
    street1 = request_json['street1']
    street2 = request_json['street2']
    pin = request_json['pin']
    company_type = request_json['company_type']
    company = Company(name,country,state,city,street1,street2,pin,company_type)
    db.session.add(company)
    db.session.commit()
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@mod_config.route('/api/customer/edit', methods=['POST'])
def api_editCustomer():
    print("Got the hit for createCustomer")
    #(self, name, country,state,city,street1,street2,pin,company_type):
    request_json = request.json
    name = request_json['name']
    country = request_json['country']
    state = request_json['state']
    city = request_json['city']
    street1 = request_json['street1']
    street2 = request_json['street2']
    pin = request_json['pin']
    company_type = request_json['company_type']
    id = int((request_json['id']))
    c = db.session.query(Company).get(id)
    c.name = name
    c.country = country
    c.state = state
    c.city = city
    c.street1 = street1
    c.street2 = street2
    c.company_type = company_type
    db.session.commit()
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@mod_config.route('/api/role/create', methods=['POST'])
def api_roleCreate():
    print("Got the hit for createuserAPI")
    request_json = request.json
    name = request_json['name']
    description = request_json['description']
    role = Role(name,description)
    db.session.add(role)
    db.session.commit()
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@mod_config.route('/api/map-role', methods=['POST'])
def api_mapRole():
    print("Got the hit for maproleAPI")
    request_json = request.json
    userID = request_json['userID']
    roleID = request_json['roleID']
    print(userID, "userID", roleID, "roleID")
    user = db.session.query(User).filter_by(id=userID).one()
    user.roleId  = roleID
    print(user)
    db.session.commit()
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@mod_config.route('/api/bank-account/create', methods=['POST'])
def api_createBank():
    print("Got hit for bank account create api")
    request_json = request.json
    print(request_json)
    ac_name = request_json['ac_name']
    ifsc = request_json['ifsc']
    swift = request_json['swift']
    iban = request_json['iban']
    bank_name = request_json['bank_name']
    branch_name = request_json['branch_name']
    ac_number = request_json['ac_number']
    owner_type = request_json['owner_type']
    ownerID = request_json['ownerID']
    #     ac_name, ac_number,ifsc, swift,iban,bank_name,branch_name,owner_type,ownerID:
    bank = BankAccount(ac_name,ac_number,ifsc,swift,iban,bank_name,branch_name,owner_type,ownerID)
    db.session.add(bank)
    db.session.commit()
    resp = jsonify(success=True)
    return resp

@mod_config.route('/api/expense-head/create', methods=['POST'])
def api_createExpenseHead():
    print("Got hit for expense head create api")
    request_json = request.json
    name = request_json['name']
    description = request_json['description']
    eh = ExpenseHead(name,description)
    db.session.add(eh)
    db.session.commit()
    resp = jsonify(success=True)
    return resp


@mod_config.route('/api/vendor/create', methods=['POST'])
def api_createVendor():
    print("Got hit for vendor create api")
    rj = request.json
    #     def __init__(self, name, country,state,city,street1,street2,pin,company_type,vendorID,beneficiary):
    vendr = Vendor(rj['name'],rj['country'],rj['state'],rj['city'],rj['street1'],rj['street2'],rj['pin'],rj['company_type'],rj['vendorID'],rj['beneficiary'])
    db.session.add(vendr)
    db.session.commit()
    resp = jsonify(success=True)
    return resp

@mod_config.route('/api/vendor/edit', methods=['POST'])
def api_editVendor():
    rj = request.json
    #     def __init__(self, name, country,state,city,street1,street2,pin,company_type,vendorID,beneficiary):
    vendr = Vendor(rj['name'],rj['country'],rj['state'],rj['city'],rj['street1'],rj['street2'],rj['pin'],rj['company_type'],rj['vendorID'],rj['beneficiary'])
    
    id = int(rj['id'])
    vendr = Vendor.query.get(id)
    vendr.name = rj['name']
    vendr.country = rj['country']
    vendr.state = rj['state']
    vendr.city = rj['city']
    vendr.street1 = rj['street1']
    vendr.street2 = rj['street2']
    vendr.pin = rj['pin']
    vendr.company_type = rj['company_type']
    vendr.vendorID = rj['vendorID']
    vendr.beneficiary = rj['beneficiary']
    db.session.commit()
    resp = jsonify(success=True)
    return resp

@mod_config.route('/api/vendor/list', methods=['GET'])
def api_VendorList():
    print("Got hit for Project create API")
    records = db.session.query(Vendor).all()
    d = []
    for item in records:
        k = []
        k.append(item.name)
        k.append(item.id)
        k.append(item.country)
        k.append(item.company_type)
        #ret = item.org_name
        d.append(k)
    resp = jsonify(data=d)
    return resp



@mod_config.route('/api/sales-entity/create', methods=['POST'])
def api_createSalesEntity():
    print("Got hit for expense head create api")
    request_json = request.json
    #    def __init__(self, name, description,uom,currency,unitprice):
    name = request_json['name']
    description = request_json['description']
    uom = request_json['uom']
    currency = request_json['currency']
    unitprice = request_json['unitprice']
    unit_type = request_json['unit_type']
    se = SalesEntity(name,description,uom,currency,unitprice,unit_type)
    db.session.add(se)
    db.session.commit()
    resp = jsonify(success=True)
    return resp

@mod_config.route('/api/project/create', methods=['POST'])
def api_createProject():
    print("Got hit for Project create API")
    request_json = request.json
    #def __init__(self, name, description,account,contact,finalQuote):
    name = request_json['name']
    description = request_json['description']
    account = request_json['account']
    contact = request_json['contact']
    finalQuote = request_json['finalQuote']
    project = Project(name,description,account,contact,finalQuote)
    db.session.add(project)
    db.session.commit()
    resp = jsonify(success=True)
    return resp

# List APIs using get requests



@mod_config.route('/api/user/list', methods=['GET'])
def api_userList():
    print("Got hit for Project create API")
    records = db.session.query(User).all()
    d = []
    for item in records:
        k = []
        k.append(item.username)
        k.append(item.id)
        k.append(item.email)
        #ret = item.org_name
        d.append(k)
    resp = jsonify(data=d)
    return resp

@mod_config.route('/api/bank-customer/list', methods=['GET'])
def api_bankCustomerList():
    print("Got hit for Project create API")
    records = db.session.query(BankAccount).all()
    # ac_name, ac_number,ifsc, swift,iban,bank_name,branch_name,owner_type,ownerID):
    d = []
    for item in records:
        k = []
        if item.owner_type == 1:
            k.append(item.ac_name)
            k.append(item.id)
            k.append(item.ac_number)
            k.append(item.bank_name)
        #ret = item.org_name
            d.append(k)
    resp = jsonify(data=d)
    return resp

@mod_config.route('/api/customer/list', methods=['GET'])
def api_CustomerList():
    print("Got hit for Project create API")
    records = db.session.query(Company).filter_by(company_type=1)
    d = []
    for item in records:
        k = []
        k.append(item.name)
        k.append(item.id)
        k.append(item.country)
        k.append(item.city)
        #ret = item.org_name
        d.append(k)
    resp = jsonify(data=d)
    return resp



@mod_config.route('/api/bank-vendor/list', methods=['GET'])
def api_bankVendorList():
    print("Got hit for Project create API")
    records = db.session.query(BankAccount).all()
    # ac_name, ac_number,ifsc, swift,iban,bank_name,branch_name,owner_type,ownerID):
    d = []
    for item in records:
        k = []
        if item.owner_type == 2:
            k.append(item.ac_name)
            k.append(item.id)
            k.append(item.ac_number)
            k.append(item.bank_name)
        #ret = item.org_name
            d.append(k)
    resp = jsonify(data=d)
    return resp

@mod_config.route('/api/bank-employee/list', methods=['GET'])
def api_bankEmployeeList():
    print("Got hit for Project create API")
    records = db.session.query(BankAccount).all()
    # ac_name, ac_number,ifsc, swift,iban,bank_name,branch_name,owner_type,ownerID):
    d = []
    for item in records:
        k = []
        if item.owner_type == 3:
            k.append(item.ac_name)
            k.append(item.id)
            k.append(item.ac_number)
            k.append(item.bank_name)
        #ret = item.org_name
            d.append(k)
    resp = jsonify(data=d)
    return resp

@mod_config.route('/api/bank-mdrift/list', methods=['GET'])
def api_bankmDriftList():
    print("Got hit for Project create API")
    records = db.session.query(BankAccount).all()
    # ac_name, ac_number,ifsc, swift,iban,bank_name,branch_name,owner_type,ownerID):
    d = []
    for item in records:
        k = []
        if item.owner_type == 4:
            k.append(item.ac_name)
            k.append(item.id)
            k.append(item.ac_number)
            k.append(item.bank_name)
        #ret = item.org_name
            d.append(k)
    resp = jsonify(data=d)
    return resp
@mod_config.route('/api/employee/create', methods=['POST'])
def api_userEmployeeCreate():
    print("Got hit for Employee Create")
    request_json = request.json
    print(request_json)
    name = request_json['name']
    username = request_json['username']
    empID = request_json['empID']
    doj = request_json['doj']
    department = request_json['department']
    role = request_json['role']
    password = request_json['password']
    email = request_json['email']
    phone = request_json['phone']
    hp = sha256_crypt.hash(request_json['password'])
    user = User(username,hp,email,role,phone,department)
    db.session.add(user)
    db.session.commit()
    print(user.id)
    dateofjoining = datetime.strptime(doj, '%Y-%m-%d')
    emp = Employee(name,empID,department,dateofjoining,user.id)
    db.session.add(emp)
    db.session.commit()
    resp = jsonify(success=True)
    return resp

@mod_config.route('/api/employee/edit', methods=['POST'])
def api_employeeEdit():
    print("Got hit for Employee Create")
    request_json = request.json
    print(request_json)
    name = request_json['name']
    username = request_json['username']
    empID = request_json['empID']
    doj = request_json['doj']
    department = request_json['department']
    role = request_json['role']
    password = request_json['password']
    email = request_json['email']
    phone = request_json['phone']
    hp = sha256_crypt.hash(request_json['password'])
    id = request_json['id']
    user = Employee.query.get(id)
    user.name = name
    user.username = username
    user.empID = empID
    user.doj = doj
    user.department = department
    user.role = role
    user.password = hp
    user.email= email
    user.phone = phone
    db.session.commit()
    print(user.id)
    resp = jsonify(success=True)
    return resp


@mod_config.route('/api/department/create', methods=['POST'])
def api_departmentCreate():
    print("Got hit for Employee Create")
    request_json = request.json
    print(request_json)
    name = request_json['name']
    description = request_json['description']
    department = Department(name,description)
    db.session.add(department)
    db.session.commit()
    resp = jsonify(succes=True)
    return resp

@mod_config.route('/api/company/create', methods=['POST'])
def api_companyCreate():
    print("Got hit for Employee Create")
    request_json = request.json
    #name, country,state,city,street1,street2,pin,company_type
    print(request_json)
    name = request_json['name']
    country = request_json['country']
    state = request_json['state']
    city = request_json['city']
    street1= request_json['street1']
    street2= request_json['street2']
    pin = request_json['pin']
    company_type = request_json['company_type']
    company = Company(name,country,state,city,street1,street2,pin,company_type)
    db.session.add(company)
    db.session.commit()
    resp = jsonify(succes=True)
    return resp
