from data.database_connect import db, ma
from flask import request
from subject_area.projects.project import project


def get_status(status_id):
    if status_id is None:
        all_data = status.query.all()
        data = statuss_schema.jsonify(all_data)
        return data
    else:
        all_data = status.query.filter_by(status_id=status_id).first()
        if all_data is None:
            return "status_id doesn't exist"
        return status_schema.jsonify(all_data)


def create_status():
    status_details = request.json.get
    status_name = status_details("status_name")
    project_id = status_details("project_id")
    if status_name is None:
        return "status_name is not defined"
    all_data1 = project.query.all()
    if [id for id in all_data1 if id.project_id == project_id]:
        data= status.query.all()
        for id in data:
            if status_name == id.status_name:
                if project_id == id.project_id:
                    return "status name and project_id combination  is already registered"


        my_update = status(status_name, project_id)
        db.session.add(my_update)
        db.session.commit()
        return {"message": "success"}
    else:
        return "project id doesn't exist"


def delete_status(status_id):
    all_data = status.query.filter_by(status_id=status_id).first()
    if all_data is None:
        return "status_id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


class status(db.Model):
    status_id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String)
    project_id = db.Column(db.Integer)

    def __init__(self, status_name, project_id):
        self.status_name = status_name
        self.project_id = project_id


class statusSchema(ma.Schema):
    class Meta:
        fields = ("status_id", "status_name", "project_id")


status_schema = statusSchema()
statuss_schema = statusSchema(many=True)


def update_status(status_id):
    data = status.query.filter_by(status_id=status_id).first()

    if data is None:
        return "status_id doesn't exist"
    status_details = request.json.get
    status_name = status_details("status_name")
    project_id = status_details("project_id")
    result = status_schema.dump(data)


    if status_name is None:
        status_name = result["status_name"]
    if project_id is None:
        project_id = result["project_id"]
    query1= project.query.all()

    if [id for id in query1 if id.project_id == project_id]:
        query = status.query.all()
        for id in query:
            if status_name == id.status_name:
                if project_id == id.project_id:
                    return "status name and project_id combination  is already registered"
        data.status_name = status_name
        data.project_id = project_id
        db.session.commit()
        return {"message": "success"}
    else:
        return "project  id doesn't exist"



