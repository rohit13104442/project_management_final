from data.database_connect import db, ma
from flask import request
from subject_area.projects.project import project
from subject_area.users_roles.user_account import user_account, user_account_schema,users_account_schema



def create_project_manager():
    project_manager_details = request.json.get
    project_id = project_manager_details("project_id")
    user_account_id = project_manager_details("user_account_id")

    if project_id is None:
        return "project id is not defined"
    if user_account_id is None:
        return "user account id is not defined"


    query1 = project.query.all()
    query2 = user_account.query.all()

    def fun(query1,query2):
        x=True
        while x==True :
            if [id for id in query1 if id.project_id == project_id]: x=True
            else: return "error1"
            if [id for id in query2 if id.user_account_id == user_account_id]: x=True
            else: return "error2"
            break
        return True
    if fun(query1, query2) is True:
        all_data = project_manager.query.all()
        for id in all_data:
            if project_id == id.project_id:
                if user_account_id == id.user_account_id:
                    return "team_id and employee_id combination  is already registered"
        query3 = user_account.query.get(user_account_id)
        x= user_account_schema.dump(query3)["is_project_manager"]
        if x != True:
            return "is_project_manager is not true in user_account"


        my_update = project_manager(project_id, user_account_id)

        db.session.add(my_update)
        db.session.commit()
        return {"message": "success"}
    elif fun(query1, query2) == "error1":
        return "project id doesn't exist"
    elif fun(query1, query2) == "error2":
        return "user_account id doesn't exist"

    else : return ("error")

def delete_project_manager(project_manager_id):
    all_data = project_manager.query.filter_by(project_manager_id=project_manager_id).first()
    if all_data is None:
        return "project_manager_id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


def update_project_manager(project_manager_id):
    data = project_manager.query.filter_by(project_manager_id=project_manager_id).first()

    if data is None:
        return "project_manager_id doesn't exist"
    project_manager_details = request.json.get
    project_id = project_manager_details("project_id")
    user_account_id = project_manager_details("user_account_id")


    result = project_manager_schema.dump(data)
    if project_id is None:
        project_id = result["project_id"]
    if user_account_id is None:
        user_account_id = result["user_account_id"]

    query1 = project.query.all()
    query2 = user_account.query.all()


    def fun(query1, query2):
        x = True
        while x == True:
            if [id for id in query1 if id.project_id == project_id]:
                x = True
            else:
                return "error1"
            if [id for id in query2 if id.user_account_id == user_account_id]:
                x = True
            else:
                return "error2"
            break
        return True

    if fun(query1, query2) is True:
        query3 = user_account.query.get(user_account_id)
        x = user_account_schema.dump(query3)["is_project_manager"]
        if x != True:
            return "is_project_manager is not true in user_account"

        data.project_id = project_id
        data.user_account_id = user_account_id
        db.session.commit()
        return {"message": "success"}
    elif fun(query1, query2) == "error1":
        return "project id doesn't exist"
    elif fun(query1, query2) == "error2":
        return "user_account id doesn't exist"
    else:
        return "error"





class project_manager(db.Model):
    project_manager_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer)
    user_account_id = db.Column(db.Integer)

    def __init__(self, project_id, user_account_id):
        self.project_id = project_id
        self.user_account_id = user_account_id


class project_managerSchema(ma.Schema):
    class Meta:
        fields = ("project_manager_id", "project_id", "user_account_id")


project_manager_schema = project_managerSchema()
projects_manager_schema = project_managerSchema(many=True)
