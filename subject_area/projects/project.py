from data.database_connect import db, ma
from flask import request




def get_project(project_id):
    if project_id is None:
        all_data = project.query.all()
        data = projects_schema.jsonify(all_data)
        return data
    else:

        all_data = project.query.filter_by(project_id=project_id).first()
        if all_data is None:
            return "project id doesn't exist"
        return project_schema.jsonify(all_data)


def create_project():
    project_name = request.json.get("project_name")
    planned_start_date = request.json.get("planned_start_date")
    planned_end_date = request.json.get("planned_end_date")
    # actual_start_date = request.json.get("actual_start_date")
    # actual_end_date = request.json.get("actual_end_date")
    project_description = request.json.get("project_description")

    if project_name is None:
        return "project_name is not defined"
    if planned_start_date is None:
        return "planned_start_date is not defined"
    if planned_end_date is None:
        return "planned_end_date is not defined"
    if project_description is None:
        return "project_description is not defined"

    my_update = project(project_name, planned_start_date, planned_end_date, project_description)
    db.session.add(my_update)
    db.session.commit()
    return {"message": "success"}


def delete_project(project_id):
    all_data = project.query.filter_by(project_id=project_id).first()
    if all_data is None:
        return "project_id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


class project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String)
    planned_start_date = db.Column()
    planned_end_date = db.Column()
    actual_start_date = db.Column()
    actual_end_date = db.Column()
    project_description = db.Column(db.TEXT)

    def __init__(self, project_name, planned_start_date, planned_end_date, project_description):
        self.project_name = project_name
        self.planned_start_date = planned_start_date
        self.planned_end_date = planned_end_date
        self.project_description = project_description



class projectSchema(ma.Schema):
    class Meta:
        fields = ("project_id", "project_name", "planned_start_date", "planned_end_date", "actual_start_date", "actual_end_date", "project_description")


project_schema = projectSchema()
projects_schema = projectSchema(many=True)


def update_project(project_id):
    data = project.query.filter_by(project_id=project_id).first()
    if data is None:
        return "project id doesn't exist"
    project_name = request.json.get("project_name")
    planned_start_date = request.json.get("planned_start_date")
    planned_end_date = request.json.get("planned_end_date")
    actual_start_date = request.json.get("actual_start_date")
    actual_end_date = request.json.get("actual_end_date")
    project_description = request.json.get("project_description")

    result = project_schema.dump(data)


    if project_name is None:
        project_name = result["project_name"]
    if planned_start_date is None:
        planned_start_date = result["planned_start_date"]
    if planned_end_date is None:
        planned_end_date = result["planned_end_date"]
    if actual_start_date is None:
        actual_start_date = result["actual_start_date"]
    if actual_end_date is None:
        actual_end_date = result["actual_end_date"]
    if project_description is None:
        project_description = result["project_description"]

    data.project_name = project_name
    data.planned_start_date = planned_start_date
    data.planned_end_date = planned_end_date
    data.actual_start_date = actual_start_date
    data.actual_end_date = actual_end_date
    data.project_description = project_description

    db.session.commit()
    return {"message": "success"}
