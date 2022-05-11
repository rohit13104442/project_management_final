from data.database_connect import db, ma
from flask import request
from subject_area.projects.project import project






def get_task(task_id):
    if task_id is None:
        all_data = task.query.all()
        data = tasks_schema.jsonify(all_data)
        return data
    else:

        all_data = task.query.filter_by(task_id=task_id).first()
        if all_data is None:
            return "task id doesn't exist"
        return task_schema.jsonify(all_data)



def create_task():
    task_details = request.json.get
    task_name = task_details("task_name")
    project_id = task_details("project_id")
    priority = task_details("priority")
    description = task_details("description")
    planned_start_date = task_details("planned_start_date")
    planned_end_date = task_details("planned_end_date")
    planned_budget = task_details("planned_budget")





    if task_name is None:
        return "task_name is not defined"
    if project_id is None:
        return "project_id is not defined"
    if priority is None:
        return "priority is not defined"
    if description is None:
        return "description is not defined"
    if planned_start_date is None:
        return "planned start date is not defined"
    if planned_end_date is None:
        return "planned end date is not defined"
    if planned_budget is None:
        return "planned budget is not defined"
    if status_id is None:
        return "status id is not defined"


    query1 = project.query.all()


    def fun(query1):
        x = True
        while x == True:
            if [id for id in query1 if id.project_id == project_id]:
                x = True
            else:
                return "error1"

            break
        return True
    if fun(query1) is True:
        my_update = task(task_name, project_id, priority, description, planned_start_date, planned_end_date,
                         planned_budget)
        db.session.add(my_update)
        db.session.commit()
        return {"message": "success"}

    elif fun(query1) == "error1":
        return "project id doesn't exist"


    else:
        return ("error")


def delete_task(task_id):
    all_data = task.query.filter_by(task_id=task_id).first()
    if all_data is None:
        return "task id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


def update_task(task_id):
    data = task.query.filter_by(task_id=task_id).first()

    if data is None:
        return "task id doesn't exist"
    task_details = request.json.get
    task_name = task_details("task_name")
    project_id = task_details("project_id")
    priority = task_details("priority")
    description = task_details("description")
    planned_start_date = task_details("planned_start_date")
    planned_end_date = task_details("planned_end_date")
    planned_budget = task_details("planned_budget")
    actual_start_date = task_details("actual_start_date")
    actual_end_date = task_details("actual_end_date")
    actual_budget = task_details("actual_budget")

    result = task_schema.dump(data)
    if task_name is None:
        task_name = result["task_name"]
    if project_id is None:
        project_id = result["project_id"]
    if priority is None:
        priority = result["priority"]
    if description is None:
        description = result["description"]
    if planned_start_date is None:
        planned_start_date = result["planned_start_date"]
    if planned_end_date is None:
        planned_end_date = result["planned_end_date"]
    if planned_budget is None:
        planned_budget = result["planned_budget"]
    if actual_start_date is None:
        actual_start_date = result["actual_start_date"]
    if actual_end_date is None:
        actual_end_date = result["actual_end_date"]
    if actual_budget is None:
        actual_budget = result["actual_budget"]



    query1 = project.query.all()


    def fun(query1):
        x = True
        while x == True:
            if [id for id in query1 if id.project_id == project_id]:
                x = True
            else:
                return "error1"

            break
        return True

    if fun(query1) is True:
        data.task_name = task_name
        data.project_id = project_id
        data.priority = priority
        data.description = description
        data.planned_start_date = planned_start_date
        data.planned_end_date = planned_end_date
        data.planned_budget = planned_budget
        data.actual_start_date = actual_start_date
        data.actual_end_date = actual_end_date
        data.actual_budget = actual_budget


        db.session.commit()
        return {"message": "success"}

    elif fun(query1) == "error1":
        return "project id doesn't exist"

    else:
        return ("error")












class task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String)
    project_id = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    description = db.Column(db.TEXT)
    planned_start_date = db.Column()
    planned_end_date = db.Column()
    planned_budget = db.Column(db.NUMERIC)
    actual_start_date = db.Column()
    actual_end_date = db.Column()
    actual_budget = db.Column(db.NUMERIC)
    status_id = db.Column(db.Integer)

    def __init__(self, task_name, project_id, priority, description, planned_start_date, planned_end_date, planned_budget):
        self.task_name = task_name
        self.project_id = project_id
        self.priority = priority
        self.description = description
        self.planned_start_date = planned_start_date
        self.planned_end_date = planned_end_date
        self.planned_budget = planned_budget
        # self.actual_start_date = actual_start_date
        # self.actual_end_date = actual_end_date
        # self.actual_budget = actual_budget


class taskSchema(ma.Schema):
    class Meta:
        fields = ("task_id","task_name", "project_id", "priority", "description", "planned_start_date", "planned_end_date", "planned_budget", "actual_start_date", "actual_end_date", "actual_budget")

task_schema = taskSchema()
tasks_schema = taskSchema(many=True)