from data.database_connect import db, ma
from flask import request
from flask_restx import  Resource, fields, Namespace
from subject_area.task_activity.activity import activity
from subject_area.task_activity.assigned import assigned


class progress_table(db.Model):
    progress_table_id = db.Column(db.Integer, primary_key = True)
    activity_id = db.Column(db.Integer)
    date = db.Column()
    assigned_id = db.Column(db.Integer)
    completed = db.Column(db.Boolean)
    reviewed = db.Column(db.Boolean)

    def __init__(self,activity_id, date, assigner_id, completed, reviewed):
        self.activity_id = activity_id
        self.date = date
        self.assigned_id = assigner_id
        self.completed = completed
        self.reviewed = reviewed

class progress_tableSchema(ma.Schema):
    class Meta:
        fields = ("progress_table_id", "activity_id", "date", "assigned_id", "completed", "reviewed")

progress_table_schema = progress_tableSchema()
progresss_table_schema = progress_tableSchema(many=True)


def get_progress_table(progress_table_id):
    if progress_table_id is None:
        all_data = progress_table.query.all()
        data = progresss_table_schema.jsonify(all_data)
        return data
    else:

        all_data = progress_table.query.filter_by(progress_table_id=progress_table_id).first()
        if all_data is None:
            return "progress_table id doesn't exist"
        return progress_table_schema.jsonify(all_data)

def update_progress_table(progress_table_id):
    data = progress_table.query.filter_by(progress_table_id=progress_table_id).first()

    if data is None:
        return "progress_table id doesn't exist"
    progress_table_details = request.json.get

    activity_id = progress_table_details("activity_id")
    date = progress_table_details("date")
    assigned_id = progress_table_details("assigned_id")
    completed = progress_table_details("completed")
    reviewed = progress_table_details("reviewed")
    result = progress_table_schema.dump(data)


    if activity_id is None:
        activity_id = result["activity_id"]
    if date is None:
        date = result["date"]
    if assigned_id is None:
        assigned_id = result["assigned_id"]
    if completed is None:
        completed = result["completed"]
    if reviewed is None:
        reviewed = result["reviewed"]
    query3 = activity.query.all()
    query4 = assigned.query.all()
    data = activity.query.filter_by(activity_id=activity_id).first()
    if date != data.planned_start_date:
        if date <= data.planned_start_date:
            return "date cant be smaller then planned start date"
        if date >= data.planned_end_date:
            return "date cant be greater then planned end date"

    def fun(query3, query4):
        x = True
        while x == True:
            if [id for id in query3 if id.activity_id == activity_id]:
                x = True
            else:
                return "error1"
            if [id for id in query4 if id.assigned_id == assigned_id]:
                x = True
            else:
                return "error2"
            break
        return True

    if fun(query3, query4) is True:
        all_data = progress_table.query.all()
        for id in all_data:
            if date == id.date:
                print(date, id.date)
                if activity_id == id.activity_id:
                    return "date and activity_id combination  is already registered"
        data.activity_id = activity_id
        data.date = date
        data.assigned_id = assigned_id
        data.completed= completed
        data.reviewed = reviewed
        db.session.commit()
        return {"message": "success"}

    elif fun(query3, query4) == "error1":
        return "activity id doesn't exist"
    elif fun(query3, query4) == "error2":
        return "assigned_id id doesn't exist"

    else:
        return ("error")

def delete_progress_table(progress_table_id):
    all_data = progress_table.query.filter_by(progress_table_id=progress_table_id).first()
    if all_data is None:
        return "progress_table doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}

def create_progress_table():
    progress_table_details = request.json.get
    activity_id = progress_table_details("activity_id")
    date = progress_table_details("date")

    assigned_id = progress_table_details("assigned_id")
    completed = progress_table_details("completed")
    reviewed = progress_table_details("reviewed")



    query3 = activity.query.all()
    query4 = assigned.query.all()
    data = activity.query.filter_by(activity_id=activity_id).first()
    if date != data.planned_start_date:
        if date <= data.planned_start_date :
            return "date cant be smaller then planned start date"
        if date >= data.planned_end_date:
            return "date cant be greater then planned end date"


    def fun(query3, query4):
        x = True
        while x == True:
            if [id for id in query3 if id.activity_id == activity_id]:
                x = True
            else:
                return "error1"
            if [id for id in query4 if id.assigned_id == assigned_id]:
                x = True
            else:
                return "error2"
            break
        return True

    if fun(query3, query4) is True:
        all_data = progress_table.query.all()
        for id in all_data:
            if date == id.date:
                if activity_id == id.activity_id:
                    return "date and activity_id combination  is already registered"
        my_update= progress_table(activity_id,date,assigned_id,completed, reviewed)
        db.session.add(my_update)
        db.session.commit()
        return {"message": "success"}

    elif fun(query3, query4) == "error1":
        return "activity id doesn't exist"
    elif fun(query3, query4) == "error2":
        return "assigned_id id doesn't exist"

    else:
        return ("error")


progress_table_ns = Namespace("progress_table", description="progress_table details")


@progress_table_ns.route("/")
class getProgress_table(Resource):
    @progress_table_ns.doc(security='apikey')
    def get(self):
        progress_table_id = None
        return get_progress_table(progress_table_id)

    POST_DOC_MODEL = progress_table_ns.model('add_progress_table', {
        'activity_id': fields.Integer(example=1,
                                      description=''),
        'date': fields.Date(example="2022-12-30",
                                          description=''),
        'assigned_id': fields.Integer(example=1,
                                          description=''),
        'completed': fields.Boolean(example="true",
                                          description='true or false'),
        'reviewed': fields.Boolean(example="false",
                                    description='true or false')
    })

    @progress_table_ns.expect(POST_DOC_MODEL)
    @progress_table_ns.doc(security='apikey')
    def post(self):
        return create_progress_table()


@progress_table_ns.route("/<int:progress_table_id>")
class getProject_id(Resource):
    @progress_table_ns.doc(security='apikey')
    def get(self, progress_table_id):
        return get_progress_table(progress_table_id)
    @progress_table_ns.doc(security='apikey')
    def delete(self, progress_table_id):
        return delete_progress_table(progress_table_id)

    PUT_DOC_MODEL = progress_table_ns.model('update_progress_table', {
        'activity_id': fields.Integer(example=1,
                                      description=''),
        'date': fields.Date(example="2022-12-30",
                            description=''),
        'assigned_id': fields.Integer(example=1,
                                   description=''),
        'completed': fields.Boolean(example="true",
                                    description='true or false'),
        'reviewed': fields.Boolean(example="false",
                                   description='true or false')
    })

    @progress_table_ns.expect(PUT_DOC_MODEL)
    @progress_table_ns.doc(security='apikey',params={"progress_table_id": "enter progress table id"})
    def put(self, progress_table_id):
        return update_progress_table(progress_table_id)

