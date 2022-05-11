from data.database_connect import db, ma
from flask import request
from datetime import date


def get_user_account(Username):
    if Username is None:
        all_data = user_account.query.all()
        data = users_account_schema.jsonify(all_data)
        return data
    else:

        all_data = user_account.query.filter_by(username=Username).first()
        if all_data is None:
            return "username doesn't exist"
        return user_account_schema.jsonify(all_data)


def create_user_account():
    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")
    first_name = request.json.get("first_name")
    last_name = request.json.get("last_name")
    is_project_manager = request.json.get("is_project_manager")
    registration_date = request.json.get("registration_date")
    is_active = request.json.get("is_active")
    if username is None:
        return "key username is not defined"
    if password is None:
        return "password is not defined"
    if email is None:
        return "email is not defined"
    if first_name is None:
        return "first_name is not defined"
    if last_name is None:
        return "last_name is not defined"
    if is_project_manager is None:
        return "is project manager - True or False"
    if is_active is None:
        return "is user active ? - True or False"
    all_data = user_account.query.all()
    for id in all_data:
        if username == id.username:
            return "username  already registered"
        elif email == id.email:
            return "email already registered"
    my_update = user_account(username, password, email, first_name, last_name, is_project_manager,
                             registration_date, is_active)

    db.session.add(my_update)
    db.session.commit()
    return {"message": "success"}


def delete_user_account(Username):
    all_data = user_account.query.filter_by(username=Username).first()
    if all_data is None:
        return "username doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


class user_account(db.Model):
    user_account_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    is_project_manager = db.Column(db.Boolean(255))
    registration_date = db.Column(db.Date, default=date.today())
    is_active = db.Column(db.Boolean(255))


    def __init__(self, username, password, email, first_name, last_name, is_project_manager, registration_date, is_active):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.is_project_manager = is_project_manager
        self.registration_date = registration_date
        self.is_active = is_active


class user_accountSchema(ma.Schema):
    class Meta:
        fields = ("user_account_id", "username", "password", "email", "first_name", "last_name", "is_project_manager", "registration_date", "is_active")


user_account_schema = user_accountSchema()
users_account_schema = user_accountSchema(many=True)


def update_user_account(Username):
    data = user_account.query.filter_by(username=Username).first()
    if data is None:
        return "username doesn't exist"
    user_account_details = request.json.get
    username = user_account_details("username")
    password = user_account_details("password")
    email = user_account_details("email")
    first_name = user_account_details("first_name")
    last_name = user_account_details("last_name")
    is_project_manager = user_account_details("is_project_manager")
    is_active = user_account_details("is_active")

    result = user_account_schema.dump(data)
    all_data = user_account.query.all()
    for id in all_data:
        if username == id.username and username != Username:
            return "username  is already registered"
        elif email == id.email:
            return "email already registered"

    if username is None:
        username = result["username"]
    if password is None:
        password = result["password"]
    if email is None:
        email = result["email"]
    if first_name is None:
        first_name = result["first_name"]
    if last_name is None:
        last_name = result["last_name"]
    if is_project_manager is None:
        is_project_manager = result["is_project_manager"]
    if is_active is None:
        is_active = result["is_active"]

    data.username = username
    data.password = password
    data.email = email
    data.first_name = first_name
    data.last_name = last_name
    data.is_project_manager = is_project_manager
    data.is_active = is_active

    db.session.commit()
    return {"message": "success"}
