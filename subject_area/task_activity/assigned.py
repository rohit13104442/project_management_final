from data.database_connect import db, ma
from flask import request
from subject_area.task_activity.activity import activity
from subject_area.users_roles.role import role
from subject_area.users_roles.employee import employee
from subject_area.users_roles.team_member import team_member
from subject_area.users_roles.team import team

def create_assigned():
    assigned_details = request.json.get
    activity_id = assigned_details("activity_id")
    role_id = assigned_details("role_id")
    employee_id = assigned_details("employee_id")

    if activity_id is None:
        return "activity id is not defined"
    if role_id is None:
        return "role id is not defined"
    if employee_id is None:
        return "employee id is not defined"


    query1 = activity.query.all()
    query2 = role.query.all()
    query3 = employee.query.all()
    def fun(query1,query2,query3):
        x=True
        while x==True :
            if [id for id in query1 if id.activity_id == activity_id]: x=True
            else: return "error1"
            if [id for id in query2 if id.role_id == role_id]: x=True
            else: return "error2"
            if [id for id in query3 if id.employee_id == employee_id]: x=True
            else: return "error3"
            break
        return True
    if fun(query1, query2, query3) is True:
        all_data = assigned.query.all()
        for id in all_data:
            if activity_id == id.activity_id:
                if role_id == id.role_id:
                    if  employee_id == id.employee_id:
                        return "activity_id and employee_id and role_id combination  is already registered"

        my_update = assigned(activity_id, role_id, employee_id)

        db.session.add(my_update)
        db.session.commit()
        return {"message": "success"}
    elif fun(query1, query2, query3) == "error1":
        return "activity id doesn't exist"
    elif fun(query1, query2, query3) == "error2":
        return "role id doesn't exist"
    elif fun(query1, query2, query3) == "error3":
        return "employee id doesn't exist"
    else : return ("error")

def create_assign_team():
    team_id = request.json.get("team_id")
    activity_id = request.json.get("activity_id")

    if activity_id is None:
        return "activity id is not defined"
    if team_id is None:
        return "team id is not defined"
    query2 = team.query.all()
    query1 = activity.query.all()

    def fun(query1, query2):
        x = True
        while x == True:
            if [id for id in query1 if id.activity_id == activity_id]:
                x = True
            else:
                return "error1"
            if [id for id in query2 if id.team_id == team_id]:
                x = True
            else:
                return "error2"
            break
        return True

    if fun(query1, query2) is True:


        fetch = team_member.query.filter_by(team_id=team_id).all()
        for id in fetch:
            all_data = assigned.query.all()
            for x in all_data:
                if activity_id == x.activity_id:
                    if id.role_id == x.role_id:
                        if id.employee_id == x.employee_id:
                            return "activity_id and employee_id and role_id combination  is already registered"
            my_update = assigned(activity_id, id.role_id, id.employee_id)

            db.session.add(my_update)
            db.session.commit()
        return {"message": "success"}
    elif fun(query1, query2) == "error1":
        return "activity id doesn't exist"
    elif fun(query1, query2) == "error2":
        return "team id doesn't exist"

    else:
        return ("error")

    fetch= team_member.query.filter_by(team_id = team_id).all()
    for id in fetch:

        my_update = assigned(activity_id, id.role_id, id.employee_id)

        db.session.add(my_update)
        db.session.commit()
    return {"message": "success"}





def delete_assigned(assigned_id):
    all_data = assigned.query.filter_by(assigned_id=assigned_id).first()
    if all_data is None:
        return "assigned_id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


def update_assigned(assigned_id):
    data = assigned.query.filter_by(assigned_id=assigned_id).first()

    if data is None:
        return "assigned_ID doesn't exist"
    assigned_details = request.json.get
    activity_id = assigned_details("tactivity_id")
    role_id = assigned_details("role_id")
    employee_id = assigned_details("employee_id")
    result = assigned_schema.dump(data)
    if activity_id is None:
        activity_id = result["activity_id"]
    if role_id is None:
        role_id = result["role_id"]
    if employee_id is None:
        employee_id = result["employee_id"]

    query1 = activity.query.all()
    query2 = role.query.all()
    query3 = employee.query.all()

    def fun(query1, query2, query3):
        x = True
        while x == True:
            if [id for id in query1 if id.activity_id == activity_id]:
                x = True
            else:
                return "error1"
            if [id for id in query2 if id.role_id == role_id]:
                x = True
            else:
                return "error2"
            if [id for id in query3 if id.employee_id == employee_id]:
                x = True
            else:
                return "error3"
            break
        return True

    if fun(query1, query2, query3) is True:
        all_data = assigned.query.all()
        for id in all_data:
            if activity_id == id.activity_id:
                if role_id == id.role_id:
                    if employee_id == id.employee_id:
                        return "activity_id and employee_id combination and role id  is already registered"
        data.activity_id = activity_id
        data.role_id = role_id
        data.employee_id = employee_id
        db.session.commit()
        return {"message": "success"}
    elif fun(query1, query2, query3) == "error1":
        return "activity id doesn't exist"
    elif fun(query1, query2, query3) == "error2":
        return "role id doesn't exist"
    elif fun(query1, query2, query3) == "error3":
        return "employee id doesn't exist"
    else:
        return ("error")


class assigned(db.Model):
    assigned_id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)
    employee_id = db.Column(db.Integer)





    def __init__(self, activity_id, role_id, employee_id):
        self.activity_id = activity_id
        self.role_id = role_id
        self.employee_id = employee_id


class assignedSchema(ma.Schema):
    class Meta:
        fields = ("assigned_id", "activity_id", "role_id", "employee_id", "active_status")


assigned_schema = assignedSchema()
assigneds_schema = assignedSchema(many=True)
