from data.database_connect import db, ma
from flask import request

def get_role(role_id):
    if role_id is None:
        all_data = role.query.all()
        data = roles_schema.jsonify(all_data)
        return data
    else:
        all_data = role.query.filter_by(role_id=role_id).first()
        if all_data is None:
            return "role id code doesn't exist"
        return role_schema.jsonify(all_data)


def create_role():
    role_details = request.json.get

    role_name = role_details("role_name")

    if role_name is None:
        return "role name is not defined"

    all_data = role.query.all()
    for id in all_data:
        if role_name == id.role_name:
            return "role name already registered"
    my_update = role(role_name)
    db.session.add(my_update)
    db.session.commit()
    return {"message": "success"}

def delete_role(role_id):
    all_data = role.query.filter_by(role_id=role_id).first()
    if all_data is None:
        return "role id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


def update_role(role_id):
    data = role.query.filter_by(role_id=role_id).first()

    if data is None:
        return "role id doesn't exist"
    role_details = request.json.get
    role_name = role_details("role_name")

    result = role_schema.dump(data)
    if role_name is None:
        role_name = result["role_name"]
    all_data = role.query.all()
    for id in all_data:
        if role_name == id.role_name:
            return "role name already registered"
    data.role_name = role_name
    db.session.commit()
    return {"message": "success"}
class role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String)

    def __init__(self,  role_name):
        self.role_name = role_name


class roleSchema(ma.Schema):
    class Meta:
        fields = ("role_id", "role_name")


role_schema = roleSchema()
roles_schema = roleSchema(many=True)