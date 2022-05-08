from data.database_connect import db, ma
from flask import request
from subject_area.task_activity.task import task


def get_activity(activity_id):
    if activity_id is None:
        all_data = activity.query.all()
        data = activitys_schema.jsonify(all_data)
        return data
    else:

        all_data = activity.query.filter_by(activity_id=activity_id).first()
        if all_data is None:
            return "activity id doesn't exist"
        return activity_schema.jsonify(all_data)


def create_activity():
    activity_details = request.json.get
    activity_name = activity_details("activity_name")
    task_id = activity_details("task_id")
    priority = activity_details("priority")
    description = activity_details("description")
    planned_start_date = activity_details("planned_start_date")
    planned_end_date = activity_details("planned_end_date")
    planned_budget = activity_details("planned_budget")

    if activity_name is None:
        return "activity_name is not defined"
    if task_id is None:
        return "task_id is not defined"
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
    query1 = task.query.all()
    if [id for id in query1 if id.project_id == task_id]:
        my_update = activity(activity_name, task_id, priority, description, planned_start_date, planned_end_date,
                             planned_budget)
        db.session.add(my_update)
        db.session.commit()
        return {"message": "success"}


    else:
        return "task id doesn't exist"



def delete_activity(activity_id):
    all_data = activity.query.filter_by(activity_id=activity_id).first()
    if all_data is None:
        return "activity id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


def update_activity(activity_id):
    data = activity.query.filter_by(activity_id=activity_id).first()

    if data is None:
        return "activity id doesn't exist"
    activity_details = request.json.get
    activity_name = activity_details("activity_name")
    task_id = activity_details("task_id")
    priority = activity_details("priority")
    description = activity_details("description")
    planned_start_date = activity_details("planned_start_date")
    planned_end_date = activity_details("planned_end_date")
    planned_budget = activity_details("planned_budget")
    actual_start_date = activity_details("actual_start_date")
    actual_end_date = activity_details("actual_end_date")
    actual_budget = activity_details("actual_budget")
    result = activity_schema.dump(data)
    if activity_name is None:
        activity_name = result["activity_name"]
    if task_id is None:
        task_id = result["task_id"]
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

    query1 = task.query.all()
    if [id for id in query1 if id.project_id == task_id]:
        data.activity_name = activity_name
        data.task_id = task_id
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

    else:
        return "task id doesn't exist"




class activity(db.Model):
    activity_id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String)
    task_id = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    description = db.Column(db.TEXT)
    planned_start_date = db.Column()
    planned_end_date = db.Column()
    planned_budget = db.Column(db.NUMERIC)
    actual_start_date = db.Column()
    actual_end_date = db.Column()
    actual_budget = db.Column(db.NUMERIC)

    def __init__(self, activity_name, task_id, priority, description, planned_start_date, planned_end_date, planned_budget):
        self.activity_name = activity_name
        self.task_id = task_id
        self.priority = priority
        self.description = description
        self.planned_start_date = planned_start_date
        self.planned_end_date = planned_end_date
        self.planned_budget = planned_budget
        # self.actual_start_date = actual_start_date
        # self.actual_end_date = actual_end_date
        # self.actual_budget = actual_budget


class activitySchema(ma.Schema):
    class Meta:
        fields = ("activity_id","activity_name", "task_id", "priority", "description", "planned_start_date", "planned_end_date", "planned_budget", "actual_start_date", "actual_end_date", "actual_budget")


activity_schema = activitySchema()
activitys_schema = activitySchema(many=True)