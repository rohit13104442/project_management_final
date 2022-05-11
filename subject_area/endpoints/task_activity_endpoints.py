from flask_restx import Resource, fields, Namespace
from subject_area.task_activity.task import get_task, create_task, delete_task, update_task
from subject_area.task_activity.activity import get_activity, create_activity, delete_activity, update_activity
from subject_area.task_activity.assigned import create_assigned, delete_assigned, update_assigned, create_assign_team

# end points for task_activity<> task
task_ns = Namespace("task", description="task details")


@task_ns.route("/")
class gettask(Resource):
    def get(self):
        task_id = None
        return get_task(task_id)

    POST_DOC_MODEL = task_ns.model('add_task', {
        'task_name': fields.String(example="task1",
                                   description='name of the task'),
        'project_id': fields.Integer(example="1",
                                     description='project id'),
        'priority': fields.Integer(example="1",
                                   description='priority from 1 to 5'),
        'description': fields.String(example="description about the task",
                                     description=''),
        'planned_start_date': fields.Date(example="2022-12-30",
                                          description='planned start date'),
        'planned_end_date': fields.Date(example="2022-12-30",
                                        description='planned end date'),
        'planned_budget': fields.Integer(example="1000",
                                         description='budget in INR')
    })

    @task_ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_task()


@task_ns.route("/<int:task_id>")
class gettask_id(Resource):
    def get(self, task_id):
        return get_task(task_id)

    def delete(self, task_id):
        return delete_task(task_id)

    PUT_DOC_MODEL = task_ns.model('update_task', {
        'task_name': fields.String(example="task1",
                                   description='name of the task'),
        'project_id': fields.Integer(example="1",
                                     description='project id'),
        'priority': fields.Integer(example="1",
                                   description='priority from 1 to 5'),
        'description': fields.String(example="description about the task",
                                     description=''),
        'planned_start_date': fields.Date(example="2022-12-30",
                                          description='planned start date'),
        'planned_end_date': fields.Date(example="2022-12-30",
                                        description='planned end date'),
        'planned_budget': fields.Integer(example=1000,
                                         description='budget in INR'),
        'actual_start_date': fields.Date(example="2022-12-30",
                                         description='actual start date'),
        'actual_end_date': fields.Date(example="2022-12-30",
                                       description='actual end date'),
        'actual_budget': fields.Integer(example=1000,
                                        description='budget in INR')


    })

    @task_ns.expect(PUT_DOC_MODEL)
    @task_ns.doc(params={"task_id": "enter task id"})
    def put(self, task_id):
        return update_task(task_id)


# end points for task_activity<> activity
activity_ns = Namespace("activity", description="activity details")


@activity_ns.route("/")
class getactivity(Resource):
    def get(self):
        activity_id = None
        return get_activity(activity_id)

    POST_DOC_MODEL = activity_ns.model('add_activity', {
        'activity_name': fields.String(example="activity1",
                                       description='name of the activity'),
        'task_id': fields.Integer(example="1",
                                  description='task id'),
        'priority': fields.Integer(example="1",
                                   description='priority from 1 to 5'),
        'description': fields.String(example="description about the task",
                                     description=''),
        'planned_start_date': fields.Date(example="2022-12-30",
                                          description='planned start date'),
        'planned_end_date': fields.Date(example="2022-12-30",
                                        description='planned end date'),
        'planned_budget': fields.Integer(example="1000",
                                         description='budget in INR'),
        'uom': fields.String(example="kg",
                                         description='unit of measurement'),
        'goal': fields.Integer(example="25",
                                  description='what is our goal in terms of uom'),
        'status_id': fields.Integer(example="1",
                               description='status id from status table')


    })

    @activity_ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_activity()


@activity_ns.route("/<int:activity_id>")
class getactivity_id(Resource):
    def get(self, activity_id):
        return get_activity(activity_id)

    def delete(self, activity_id):
        return delete_activity(activity_id)

    PUT_DOC_MODEL = activity_ns.model('update_activity', {
        'activity_name': fields.String(example="activity1",
                                       description='name of the activity'),
        'task_id': fields.Integer(example="1",
                                  description='task id'),
        'priority': fields.Integer(example="1",
                                   description='priority from 1 to 5'),
        'description': fields.String(example="description about the task",
                                     description=''),
        'planned_start_date': fields.Date(example="2022-12-30",
                                          description='planned start date'),
        'planned_end_date': fields.Date(example="2022-12-30",
                                        description='planned end date'),
        'planned_budget': fields.Integer(example=1000,
                                         description='budget in INR'),
        'actual_start_date': fields.Date(example="2022-12-30",
                                         description='actual start date'),
        'actual_end_date': fields.Date(example="2022-12-30",
                                       description='actual end date'),
        'actual_budget': fields.Integer(example=1000,
                                        description='budget in INR'),
        'uom': fields.String(example="kg",
                             description='unit of measurement'),
        'goal': fields.Integer(example="25",
                               description='what is our goal in terms of uom'),
        'status_id': fields.Integer(example="1",
                                    description='status id from status table')

    })

    @activity_ns.expect(PUT_DOC_MODEL)
    @activity_ns.doc(params={"activity_id": "enter activityid"})
    def put(self, activity_id):
        return update_activity(activity_id)


# end points for task_activity<> assigned
assigned_ns = Namespace("assigned", description="assigned details")


@assigned_ns.route("/")
class getassigned(Resource):
    POST_DOC_MODEL = assigned_ns.model('add_assigned', {
        'activity_id': fields.Integer(example=1, description='id of the activity'),
        'role_id': fields.Integer(example=1, description='id of the role'),
        'employee_id': fields.Integer(example=1, description='id of the employee')

    })

    @assigned_ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_assigned()


@assigned_ns.route("/<int:assigned_id>")
class getassigned_id(Resource):
    def delete(self, assigned_id):
        return delete_assigned(assigned_id)

    PUT_DOC_MODEL = assigned_ns.model('update_assigned', {
        'activity_id': fields.Integer(example=1, description='id of the team'),
        'role_id': fields.Integer(example=1, description='id of the role'),
        'employee_id': fields.Integer(example=1, description='id of the employee')


    })

    @activity_ns.expect(PUT_DOC_MODEL)
    @assigned_ns.doc(params={"assigned_id": "enter assigned_id"})
    def put(self, assigned_id):
        return update_assigned(assigned_id)

@assigned_ns.route("/team")
class fetchteam(Resource):
    POST_DOC_MODEL = assigned_ns.model('add_team',{
        'team_id':fields.Integer(example=1, description="id od the team to add employee in activity"),
        'activity_id':fields.Integer(example=1, description="activity id to add team")
    })
    @assigned_ns.expect(POST_DOC_MODEL)
    def post(self):
       return create_assign_team()