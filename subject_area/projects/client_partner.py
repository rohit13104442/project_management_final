from data.database_connect import db, ma
from flask import request


def get_client_partner(client_partner_id):
    if client_partner_id is None:
        all_data = client_partner.query.all()
        data = clients_partner_schema.jsonify(all_data)
        return data
    else:

        all_data = client_partner.query.filter_by(client_partner_id=client_partner_id).first()
        if all_data is None:
            return "client_partner id doesn't exist"
        return client_partner_schema.jsonify(all_data)


def create_client_partner():
    cp_name = request.json.get("cp_name")
    cp_address = request.json.get("cp_address")
    cp_details = request.json.get("cp_details")

    if cp_name is None:
        return "client or partner name is not defined"
    if cp_address is None:
        return "client or partner address is not defined"
    if cp_details is None:
        return "client or partner details is not defined"


    my_update = client_partner (cp_name, cp_address,cp_details)
    db.session.add(my_update)
    db.session.commit()
    return {"message": "success"}


def delete_client_partner(client_partner_id):
    all_data = client_partner.query.filter_by(client_partner_id=client_partner_id).first()
    if all_data is None:
        return "client_partner_id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


def update_client_partner(client_partner_id):
    data = client_partner.query.filter_by(client_partner_id=client_partner_id).first()
    if data is None:
        return "client_partner id doesn't exist"
    cp_name = request.json.get("cp_name")
    cp_address = request.json.get("cp_address")
    cp_details = request.json.get("cp_details")

    result = client_partner_schema.dump(data)
    all_data = client_partner.query.all()

    if cp_name is None:
        cp_name = result["cp_name"]
    if cp_address is None:
        cp_address= result["cp_address"]
    if cp_details is None:
        cp_details = result["cp_details"]


    data.cp_name = cp_name
    data.cp_address = cp_address
    data.cp_details = cp_details


    db.session.commit()
    return {"message": "success"}


class client_partner(db.Model):
    client_partner_id = db.Column(db.Integer, primary_key=True)
    cp_name = db.Column(db.String)
    cp_address = db.Column(db.String)
    cp_details = db.Column(db.String)

    def __init__(self, cp_name, cp_address, cp_details):
        self.cp_name = cp_name
        self.cp_address = cp_address
        self.cp_details = cp_details


class client_partnerSchema(ma.Schema):
    class Meta:
        fields = ("client_partner_id", "cp_name", "cp_address", "cp_details")

client_partner_schema = client_partnerSchema()
clients_partner_schema = client_partnerSchema(many=True)