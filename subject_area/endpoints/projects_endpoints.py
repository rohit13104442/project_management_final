from flask_restx import  Resource, fields, Namespace
from subject_area.projects.project import get_project, delete_project, update_project, create_project
from subject_area.projects.project_manager import delete_project_manager, update_project_manager, create_project_manager
from subject_area.projects.client_partner import get_client_partner, create_client_partner, delete_client_partner, update_client_partner
from subject_area.projects.on_project import get_on_project,create_on_project,delete_on_project,update_on_project
from subject_area.projects.status import get_status, update_status, delete_status, create_status
from .validators import token_check


# end points for projects <> project
project_ns = Namespace("project", description="project details")


@project_ns.route("/")


class getProject(Resource):
    @project_ns.doc(security='apikey')
    def get(self):
        token_check()
        project_id = None
        return get_project(project_id)

    POST_DOC_MODEL = project_ns.model('add_project', {
        'project_name': fields.String(example="project1",
                                      description='name of the project'),
        'planned_start_date': fields.Date(example="2022-12-30",
                                          description='planned start date'),
        'planned_end_date': fields.Date(example="2022-12-30",
                                          description='planned end date'),
        'project_description': fields.String(example="description about the project",
                                          description='')})
    # @project_ns.doc(security ='apiKey')
    @project_ns.expect(POST_DOC_MODEL)
    @project_ns.doc(security='apikey')
    def post(self):
        return create_project()


@project_ns.route("/<int:project_id>")
class getProject_id(Resource):
    @project_ns.doc(security='apikey')
    def get(self, project_id):
        return get_project(project_id)
    @project_ns.doc(security='apikey')
    def delete(self, project_id):
        return delete_project(project_id)

    PUT_DOC_MODEL = project_ns.model('update_project', {
        'project_name': fields.String(example="project1",
                                      description='name of the project'),
        'planned_start_date': fields.Date(example="2022-12-30",
                                          description='planned start date'),
        'planned_end_date': fields.Date(example="2022-12-30",
                                        description='planned end date'),
        'actual_start_date': fields.Date(example="2022-12-30",
                                          description='actual start date'),
        'actual_end_date': fields.Date(example="2022-12-30",
                                         description='actual start date'),
        'project_description': fields.Date(example="description about the project",
                                           description='')


    })

    @project_ns.expect(PUT_DOC_MODEL)
    @project_ns.doc(security='apikey',params={"project_id": "enter project id"})
    def put(self, project_id):
        return update_project(project_id)



# end points for projects <> project_manager

project_manager_ns = Namespace("project_manager", description="project_manager details")


@project_manager_ns.route("/")
class getProject_manager(Resource):

    POST_DOC_MODEL = project_manager_ns.model('add_project_manager', {
        'project_id': fields.Integer(example="1",
                                      description='project_id'),
        'user_account_id': fields.Integer(example="1",
                                     description='user-account_id')})

    @project_manager_ns.doc(security='apikey')
    @project_manager_ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_project_manager()


@project_manager_ns.route("/<int:project_manager_id>")
class getProject_manager_id(Resource):
    @project_manager_ns.doc(security='apikey')
    def delete(self, project_manager_id):
        return delete_project_manager(project_manager_id)

    PUT_DOC_MODEL = project_manager_ns.model('update_project_manager', {
        'project_id': fields.Integer(example="1",
                                     description='project_id'),
        'user_account_id': fields.Integer(example="1",
                                          description='user-account_id')})




    @project_manager_ns.expect(PUT_DOC_MODEL)
    @project_manager_ns.doc(security='apikey',params={"project_manager_id": "enter project manager id"})
    def put(self, project_manager_id):
        return update_project_manager(project_manager_id)



# end points for projects <> client_partner
client_partner_ns = Namespace("client_partner", description="client and partner details")


@client_partner_ns.route("/")
class getClient_partner(Resource):
    @client_partner_ns.doc(security='apikey')
    def get(self):
        client_partner_id = None
        return get_client_partner(client_partner_id)

    POST_DOC_MODEL = client_partner_ns.model('add_client_partner', {
        'cp_name': fields.String(example="partner1",
                                      description='name of the client or partner'),
    'cp_address': fields.String(example="h.no 123, noida",
                                      description='address of the client or partner'),
    'cp_details': fields.String(example="freelancer",
                                      description='details of the client or partner'),
        })

    @client_partner_ns.expect(POST_DOC_MODEL)
    @client_partner_ns.doc(security='apikey')
    def post(self):
        return create_client_partner()


@client_partner_ns.route("/<int:client_partner_id>")
class getClient_partner_id(Resource):
    @client_partner_ns.doc(security='apikey')
    def get(self, client_partner_id):
        return get_client_partner(client_partner_id)
    @client_partner_ns.doc(security='apikey')
    def delete(self, client_partner_id):
        return delete_client_partner(client_partner_id)

    PUT_DOC_MODEL = client_partner_ns.model('update_client_partner', {
        'cp_name': fields.String(example="partner1",
                                      description='name of the client or partner'),
    'cp_address': fields.String(example="h.no 123, noida",
                                      description='address of the client or partner'),
    'cp_details': fields.String(example="freelancer",
                                      description='details of the client or partner')


    })

    @client_partner_ns.expect(PUT_DOC_MODEL)
    @client_partner_ns.doc(security='apikey',params={"client_partner_id": "enter client_partner id"})
    def put(self, client_partner_id):
        return update_client_partner(client_partner_id)



# end points for projects <> on_project
on_project_ns = Namespace("on_project", description="on_project details")


@on_project_ns.route("/")
class getOn_project(Resource):
    @on_project_ns.doc(security='apikey')
    def get(self):
        on_project_id = None
        return get_on_project(on_project_id)

    POST_DOC_MODEL = on_project_ns.model('add_on_project', {
        'project_id': fields.Integer(example="1",
                                      description='project id'),
        'client_partner_id': fields.Integer(example="1",
                                     description='client partner id'),
        'start_date': fields.Date(example="2022-12-30",
                                          description=' start date'),
        'is_client': fields.Boolean(example="false",
                                  description=' true or false'),
        'is_partner': fields.Boolean(example="false",
                                    description=' true or false'),

        'description': fields.Date(example="description ",
                                          description='')})

    @on_project_ns.expect(POST_DOC_MODEL)
    @on_project_ns.doc(security='apikey')
    def post(self):
        return create_on_project()


@on_project_ns.route("/<int:on_project_id>")
class getOn_project_id(Resource):
    @on_project_ns.doc(security='apikey')
    def get(self, on_project_id):
        return get_on_project(on_project_id)
    @on_project_ns.doc(security='apikey')
    def delete(self, on_project_id):
        return delete_on_project(on_project_id)

    PUT_DOC_MODEL = on_project_ns.model('update_on_project', {
        'project_id': fields.Integer(example="1",
                                     description='project id'),
        'client_partner_id': fields.Integer(example="1",
                                            description='client partner id'),
        'start_date': fields.Date(example="2022-12-30",
                                  description=' start date'),
        'end_date': fields.Date(example="2022-12-30",
                                  description=' end date'),
        'is_client': fields.Boolean(example="false",
                                    description=' true or false'),
        'is_partner': fields.Boolean(example="false",
                                     description=' true or false'),

        'description': fields.Date(example="description ",
                                   description='')})




    @on_project_ns.expect(PUT_DOC_MODEL)
    @on_project_ns.doc(security='apikey', params={"on_project_id": "enter on_project id"})
    def put(self, on_project_id):
        return update_on_project(on_project_id)


# end points for projects <> status
status_ns = Namespace("status", description="status details")


@status_ns.route("/")
class getStatus(Resource):
    @status_ns.doc(security='apikey')
    def get(self):
        status_id = None
        return get_status(status_id)

    POST_DOC_MODEL = status_ns.model('add_status', {
        'status_name': fields.String(example="completed", description=''),
        'project_id': fields.Integer(example="0", description='project id from project table')})

    @status_ns.expect(POST_DOC_MODEL)
    @status_ns.doc(security='apikey')
    def post(self):
        return create_status()


@status_ns.route("/<int:status_id>")
class getStatus_id(Resource):
    @status_ns.doc(security='apikey')
    def get(self, status_id):
        return get_status(status_id)

    @status_ns.doc(security='apikey')
    def delete(self, status_id):
        return delete_status(status_id)

    PUT_DOC_MODEL = status_ns.model('update_status', {
        'status_name': fields.String(example="completed", description=''),
        'project_id': fields.Integer(example="0", description='project id from project table')})


    @status_ns.expect(PUT_DOC_MODEL)
    @status_ns.doc(security='apikey', params={"status_id": "enter status id"})
    def put(self, status_id):
        return update_status(status_id)
