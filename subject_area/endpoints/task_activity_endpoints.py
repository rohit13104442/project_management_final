from flask_restx import Resource, fields, Namespace
from subject_area.task_activity.task import get_task, create_task, delete_task, update_task

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
                                         description='budget in INR')})

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
                                        description='budget in INR'),

    })

    @task_ns.expect(PUT_DOC_MODEL)
    @task_ns.doc(params={"task_id": "enter task id"})
    def put(self, task_id):
        return update_task(task_id)
