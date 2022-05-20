

from data.database_connect import db, ma
from flask import request
from subject_area.users_roles.team import team
from subject_area.users_roles.role import role
from subject_area.users_roles.employee import employee


def create_team_member():
    team_member_details = request.json.get
    team_id = team_member_details("team_id")
    role_id = team_member_details("role_id")
    employee_id = team_member_details("employee_id")
    active_status = team_member_details("active_status")

    if team_id is None:
        return "team id is not defined"
    if role_id is None:
        return "role id is not defined"
    if employee_id is None:
        return "employee id is not defined"


    query1 = team.query.all()
    query2 = role.query.all()
    query3 = employee.query.all()
    def fun(query1,query2,query3):
        x=True
        while x==True :
            if [id for id in query1 if id.team_id == team_id]: x=True
            else: return "error1"
            if [id for id in query2 if id.role_id == role_id]: x=True
            else: return "error2"
            if [id for id in query3 if id.employee_id == employee_id]: x=True
            else: return "error3"
            break
        return True
    if fun(query1, query2, query3) is True:
        all_data = team_member.query.all()
        for id in all_data:
            if team_id == id.team_id:
                if employee_id == id.employee_id:
                    return "team_id and employee_id combination  is already registered"

        my_update = team_member(team_id, role_id, employee_id, active_status)

        db.session.add(my_update)
        db.session.commit()
        return {"message": "success"}
    elif fun(query1, query2, query3) == "error1":
        return "team id doesn't exist"
    elif fun(query1, query2, query3) == "error2":
        return "role id doesn't exist"
    elif fun(query1, query2, query3) == "error3":
        return "employee id doesn't exist"
    else : return ("error")




def delete_team_member(team_member_id):
    all_data = team_member.query.filter_by(team_member_id=team_member_id).first()
    if all_data is None:
        return "team_member_id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


def update_team_member(team_member_id):
    data = team_member.query.filter_by(team_member_id=team_member_id).first()

    if data is None:
        return "team_member_ID doesn't exist"
    team_member_details = request.json.get
    team_id = team_member_details("team_id")
    role_id = team_member_details("role_id")
    employee_id = team_member_details("employee_id")
    active_status = team_member_details("active_status")
    result = team_member_schema.dump(data)
    if team_id is None:
        team_id = result["team_id"]
    if role_id is None:
        role_id = result["role_id"]
    if employee_id is None:
        employee_id = result["employee_id"]
    if active_status is None:
        active_status = result["active_status"]
    query1 = team.query.all()
    query2 = role.query.all()
    query3 = employee.query.all()

    def fun(query1, query2, query3):
        x = True
        while x == True:
            if [id for id in query1 if id.team_id == team_id]:
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
        data.team_id = team_id
        data.role_id = role_id
        data.employee_id = employee_id
        data.active_status = active_status
        db.session.commit()
        return {"message": "success"}
    elif fun(query1, query2, query3) == "error1":
        return "team id doesn't exist"
    elif fun(query1, query2, query3) == "error2":
        return "role id doesn't exist"
    elif fun(query1, query2, query3) == "error3":
        return "employee id doesn't exist"
    else:
        return ("error")


class team_member(db.Model):
    team_member_id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)
    employee_id = db.Column(db.Integer)
    active_status = db.Column(db.Boolean)




    def __init__(self, team_id, role_id, employee_id, active_status):
        self.team_id = team_id
        self.role_id = role_id
        self.employee_id = employee_id
        self.active_status = active_status


class team_memberSchema(ma.Schema):
    class Meta:
        fields = ("team_member_id", "team_id", "role_id", "employee_id", "active_status")


team_member_schema = team_memberSchema()
team_members_schema = team_memberSchema(many=True)
