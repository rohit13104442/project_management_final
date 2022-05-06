from data.database_connect import db, ma
from flask import request
from subject_area.projects.project import project
from subject_area.projects.client_partner import client_partner


def get_on_project(on_project_id):
    if on_project_id is None:
        all_data = on_project.query.all()
        data = ons_project_schema.jsonify(all_data)
        return data
    else:

        all_data = on_project.query.filter_by(on_project_id=on_project_id).first()
        if all_data is None:
            return "on_project id doesn't exist"
        return on_project_schema.jsonify(all_data)



def create_on_project():
    on_project_details = request.json.get
    project_id = on_project_details("project_id")
    client_partner_id = on_project_details("client_partner_id")
    start_date = on_project_details("start_date")
    # end_date = on_project_details("end_date")
    is_client = on_project_details("is_client")
    is_partner = on_project_details("is_partner")
    description = on_project_details("description")
    if project_id is None:
        return "project_id is not defined"
    if client_partner_id is None:
        return "client_partner id is not defined"
    if start_date is None:
        return "start date is not defined"
    if is_client is None:
        return "is_client is not defined"
    if is_partner is None:
        return "is_partner is not defined"
    if description is None:
        return "description is not defined"
    if is_client is False and is_partner is False:
        return "is_client and is_partner both can't be false"
    if is_client is True and is_partner is True:
        return "is_client and is_partner both can't be true"
    query1 = project.query.all()
    query2 = client_partner.query.all()

    def fun(query1, query2):
        x = True
        while x == True:
            if [id for id in query1 if id.project_id == project_id]:
                x = True
            else:
                return "error1"
            if [id for id in query2 if id.client_partner_id == client_partner_id]:
                x = True
            else:
                return "error2"
            break
        return True

    if fun(query1, query2) is True:

        my_update = on_project(project_id, client_partner_id, start_date, is_client, is_partner, description)
        db.session.add(my_update)
        db.session.commit()
        return {"message": "success"}

    elif fun(query1, query2) == "error1":
        return "project id doesn't exist"
    elif fun(query1, query2) == "error2":
        return "client_partner id doesn't exist"

    else: return ("error")




def delete_on_project(on_project_id):
    all_data = on_project.query.filter_by(on_project_id=on_project_id).first()
    if all_data is None:
        return "on_project doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


def update_on_project(on_project_id):
    data = on_project.query.filter_by(on_project_id=on_project_id).first()

    if data is None:
        return "on_project id doesn't exist"
    on_project_details = request.json.get
    project_id = on_project_details("project_id")
    client_partner_id = on_project_details("client_partner_id")
    start_date = on_project_details("start_date")
    end_date = on_project_details("end_date")
    is_client = on_project_details("is_client")
    is_partner = on_project_details("is_partner")
    description = on_project_details("description")

    result = on_project_schema.dump(data)
    if project_id is None:
        project_id = result["project_id"]
    if client_partner_id is None:
        client_partner_id = result["client_partner_id"]
    if start_date is None:
        start_date = result["start_date"]
    if end_date is None:
        end_date = result["end_date"]
    if is_client is None:
        is_client = result["is_client"]
    if is_partner is None:
        is_partner = result["is_partner"]
    if description is None:
        description = result["description"]
    if is_client is False and is_partner is False:
        return "is_client and is_partner both can't be false"
    if is_client is True and is_partner is True:
        return "is_client and is_partner both can't be true"

    query3 = project.query.all()
    query4 = client_partner.query.all()

    def fun(query3, query4):
        x = True
        while x == True:
            if [id for id in query3 if id.project_id == project_id]:
                x = True
            else:
                return "error1"
            if [id for id in query4 if id.client_partner_id == client_partner_id]:
                x = True
            else:
                return "error2"
            break
        return True

    if fun(query3, query4) is True:
        data.project_id = project_id
        data.client_partner_id = client_partner_id
        data.start_date = start_date
        data.end_date = end_date
        data.is_client = is_client
        data.is_partner = is_partner
        data.description = description
        db.session.commit()
        return {"message": "success"}

    elif fun(query3, query4) == "error1":
        return "project id doesn't exist"
    elif fun(query3, query4) == "error2":
        return "client_partner id doesn't exist"

    else:
        return ("error")


class on_project(db.Model):
    on_project_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer)
    client_partner_id = db.Column(db.Integer)
    start_date = db.Column()
    end_date = db.Column()
    is_client = db.Column(db.Boolean)
    is_partner = db.Column(db.Boolean)
    description = db.Column(db.TEXT)


    def __init__(self, project_id, client_partner_id, start_date, is_client, is_partner, description):
        self.project_id = project_id
        self.client_partner_id = client_partner_id
        self.start_date = start_date
        # self.end_date = end_date
        self.is_client = is_client
        self.is_partner = is_partner
        self.description = description


class on_projectSchema(ma.Schema):
    class Meta:
        fields = ("on_project_id","project_id", "client_partner_id", "start_date", "end_date", "is_client", "is_partner", "description")

on_project_schema = on_projectSchema()
ons_project_schema = on_projectSchema(many=True)