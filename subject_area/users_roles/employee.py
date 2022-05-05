from data.database_connect import db, ma
from flask import request
from subject_area.users_roles.user_account import user_account


def get_employee(emp_code):
    if emp_code is None:
        all_data = employee.query.all()
        data = employees_schema.jsonify(all_data)
        return data
    else:
        all_data = employee.query.filter_by(employee_code=emp_code).first()
        if all_data is None:
            return "employee code doesn't exist"
        return employee_schema.jsonify(all_data)


def create_employee():
    employee_details = request.json.get
    employee_code = employee_details("employee_code")
    employee_name = employee_details("employee_name")
    user_account_id = employee_details("user_account_id")
    if employee_code is None:
        return "employee_code is not defined"
    if employee_name is None:
        return "employee_name is not defined"
    all_data = employee.query.all()
    for id in all_data:
        if employee_code == id.employee_code:
            return "employee with this code is already registered"
    my_update = employee(employee_code, employee_name, user_account_id)
    db.session.add(my_update)
    db.session.commit()
    return {"message": "success"}


def delete_employee(emp_code):
    all_data = employee.query.filter_by(employee_code=emp_code).first()
    if all_data is None:
        return "employee_code doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


class employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_code = db.Column(db.String)
    employee_name = db.Column(db.String)
    user_account_id = db.Column(db.Integer)

    def __init__(self, employee_code, employee_name, user_account_id):
        self.employee_code = employee_code
        self.employee_name = employee_name
        self.user_account_id = user_account_id


class employeeSchema(ma.Schema):
    class Meta:
        fields = ("employee_id", "employee_code", "employee_name", "user_account_id")


employee_schema = employeeSchema()
employees_schema = employeeSchema(many=True)


def update_employee(emp_code):
    data = employee.query.filter_by(employee_code=emp_code).first()

    if data is None:
        return "employee_code doesn't exist"
    employee_details = request.json.get
    employee_code = employee_details("employee_code")
    employee_name = employee_details("employee_name")
    user_account_id = employee_details("user_account_id")
    result = employee_schema.dump(data)
    all_data = employee.query.all()

    for id in all_data:
        if employee_code == id.employee_code and employee_code != emp_code:
            return "employee with this code is already registered"

    if employee_code is None:
        employee_code = result["employee_code"]
    if employee_name is None:
        employee_name = result["employee_name"]
    if user_account_id is None:
        user_account_id = result["user_account_id"]
    query1= user_account.query.all()

    if [id for id in query1 if id.user_account_id == user_account_id]:
        data.employee_code = employee_code
        data.employee_name = employee_name
        data.user_account_id = user_account_id
        db.session.commit()
        return {"message": "success"}
    else:
        return "user account id doesn't exist"



