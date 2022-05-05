from flask_restx import Api, Resource, fields

from flask import Blueprint
from data.database_connect import app
from subject_area.users_roles.user_account import update_user_account, get_user_account, \
    delete_user_account, create_user_account
from subject_area.users_roles.employee import update_employee, create_employee, get_employee, delete_employee
from subject_area.users_roles.team import update_team, create_team, get_team, delete_team
from subject_area.users_roles.role import update_role, create_role, get_role, delete_role
from subject_area.users_roles.team_member import update_team_member, create_team_member, delete_team_member

blueprint = Blueprint('api', __name__)
api = Api(app, version='1', title='API', description='End-Points')

# end points for user_roles <> user_account
ns = api.namespace("user_account", description="user")


@ns.route("/")
class getUserAccount(Resource):
    def get(self):
        Username = None
        return get_user_account(Username)

    POST_DOC_MODEL = ns.model('add_user_account', {
        'username': fields.String(example="test",
                                  description='username of the user'),
        'password': fields.String(example="test2",
                                  description='password of the user'),

        'email': fields.String(example="test3@gmail.com",
                               description='email of the user'),
        'first_name': fields.String(example="test",
                                    description='first name of the user'),
        'last_name': fields.String(example="test4",
                                   description='last name of the user'),
        'is_project_manager': fields.Boolean(example=True,
                                             description='true or false'),
        'is_active': fields.Boolean(example=True,
                                    description='true or false')

    })

    @ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_user_account()


@ns.route("/<string:Username>")
class getUserAccount_id(Resource):
    def get(self, Username):
        return get_user_account(Username)

    def delete(self, Username):
        return delete_user_account(Username)

    PUT_DOC_MODEL = ns.model('update_user_account', {
        'username': fields.String(example="test",
                                  description='username of the user'),
        'password': fields.String(example="test2",
                                  description='password of the user'),

        'email': fields.String(example="test3@gmail.com",
                               description='email of the user'),
        'first_name': fields.String(example="test",
                                    description='first name of the user'),
        'last_name': fields.String(example="test4",
                                   description='last name of the user'),
        'is_project_manager': fields.Boolean(example=True,
                                             description='true or false'),
        'is_active': fields.Boolean(example=True,
                                    description='true or false')

    })

    @ns.expect(PUT_DOC_MODEL)
    @ns.doc(params={"Username": "enter username"})
    def put(self, Username):

        return update_user_account(Username)


# end points for user_roles <> employees
ns = api.namespace("employee", description="employee data")


@ns.route("/")
class getEmployee(Resource):
    def get(self):
        employee_code = None
        return get_employee(employee_code)

    POST_DOC_MODEL = ns.model('add_employee', {
        'employee_code': fields.String(example="code01", description='code of the employee'),
        'employee_name': fields.String(example="name", description='name of the employee')
    })

    @ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_employee()


@ns.route("/<string:emp_code>")
class getEmployee_id(Resource):
    def get(self, emp_code):
        return get_employee(emp_code)

    def delete(self, emp_code):
        return delete_employee(emp_code)

    PUT_DOC_MODEL = ns.model('update_employee', {
        'employee_code': fields.String(example="code01", description='code of the employee'),
        'employee_name': fields.String(example="name", description='name of the employee'),
        'user_account_id': fields.Integer(example="0", description='user account id from user_account table')

    })

    @ns.expect(PUT_DOC_MODEL)
    @ns.doc(params={"emp_code": "enter employee_code"})
    def put(self, emp_code):
        return update_employee(emp_code)


# end points for user_roles <> team
ns = api.namespace("team", description="team name & id")


@ns.route("/")
class getTeam(Resource):
    def get(self):
        team_id = None
        return get_team(team_id)

    POST_DOC_MODEL = ns.model('add_team', {
        'team_name': fields.String(example="name", description='name of the team')
    })

    @ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_team()


@ns.route("/<string:team_id>")
class getTeam_id(Resource):
    def get(self, team_id):
        return get_team(team_id)

    def delete(self, team_id):
        return delete_team(team_id)

    PUT_DOC_MODEL = ns.model('update_team', {

        'team_name': fields.String(example="name", description='name of the team')
    })

    @ns.expect(PUT_DOC_MODEL)
    @ns.doc(params={"team_id": "enter team id"})
    def put(self, team_id):
        return update_team(team_id)

# end points for user_roles <> role


ns = api.namespace("role", description="role name & id")


@ns.route("/")
class getRole(Resource):
    def get(self):
        role_id = None
        return get_role(role_id)

    POST_DOC_MODEL = ns.model('add_role', {
        'role_name': fields.String(example="name", description='role name')
    })

    @ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_role()


@ns.route("/<string:role_id>")
class getRole_id(Resource):
    def get(self, role_id):
        return get_role(role_id)

    def delete(self, role_id):
        return delete_role(role_id)

    PUT_DOC_MODEL = ns.model('update_role', {

        'role_name': fields.String(example="name", description='role name')
    })

    @ns.expect(PUT_DOC_MODEL)
    @ns.doc(params={"role_id": "enter role id"})
    def put(self, role_id):
        return update_role(role_id)


# end points for user_roles <> team_member
ns = api.namespace("team_member", description="team_member")


@ns.route("/")
class getTeam_member(Resource):
    POST_DOC_MODEL = ns.model('add_team_member', {
        'team_id': fields.Integer(example=1, description='id of the team'),
        'role_id': fields.Integer(example=1, description='id of the role'),
        'employee_id': fields.Integer(example=1, description='id of the employee'),
        'active_status': fields.Boolean(example= "true", description='True or False')

    })

    @ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_team_member()


@ns.route("/<int:team_member_id>")
class getTeam_member_id(Resource):
    def delete(self, team_member_id):
        return delete_team_member(team_member_id)

    PUT_DOC_MODEL = ns.model('update_team_member', {
         'team_id': fields.Integer(example=1, description='id of the team'),
        'role_id': fields.Integer(example=1, description='id of the role'),
        'employee_id': fields.Integer(example=1, description='id of the employee'),
        'active_status': fields.Boolean(example="true", description='True or False')

    })

    @ns.expect(PUT_DOC_MODEL)
    @ns.doc(params={"team_member_id": "enter team-member_id"})
    def put(self, team_member_id):
        return update_team_member(team_member_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5555)
