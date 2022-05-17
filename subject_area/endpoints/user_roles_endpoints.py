from flask_restx import Api, Resource, fields, Namespace

from flask import Blueprint

from subject_area.users_roles.user_account import update_user_account, get_user_account, \
    delete_user_account, create_user_account
from subject_area.users_roles.employee import update_employee, create_employee, get_employee, delete_employee
from subject_area.users_roles.team import update_team, create_team, get_team, delete_team
from subject_area.users_roles.role import update_role, create_role, get_role, delete_role
from subject_area.users_roles.team_member import update_team_member, create_team_member, delete_team_member

blueprint = Blueprint('api', __name__)


# end points for user_roles <> user_account
user_account_ns = Namespace("user_account", description="user")


@user_account_ns.route("/")
class getUserAccount(Resource):
    @user_account_ns.doc(security='apikey')
    def get(self):
        Username = None
        return get_user_account(Username)

    POST_DOC_MODEL = user_account_ns.model('add_user_account', {
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

    @user_account_ns.expect(POST_DOC_MODEL)
    @user_account_ns.doc(security='apikey')
    def post(self):
        return create_user_account()


@user_account_ns.route("/<string:Username>")
class getUserAccount_id(Resource):
    @user_account_ns.doc(security='apikey')
    def get(self, Username):
        return get_user_account(Username)
    @user_account_ns.doc(security='apikey')
    def delete(self, Username):
        return delete_user_account(Username)

    PUT_DOC_MODEL = user_account_ns.model('update_user_account', {
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

    @user_account_ns.expect(PUT_DOC_MODEL)
    @user_account_ns.doc(security='apikey',params={"Username": "enter username"})
    def put(self, Username):

        return update_user_account(Username)


# end points for user_roles <> employees
employee_ns = Namespace("employee", description="employee data")


@employee_ns.route("/")
class getEmployee(Resource):
    @employee_ns.doc(security='apikey')
    def get(self):
        employee_code = None
        return get_employee(employee_code)

    POST_DOC_MODEL = employee_ns.model('add_employee', {
        'employee_code': fields.String(example="code01", description='code of the employee'),
        'employee_name': fields.String(example="name", description='name of the employee')
    })
    @employee_ns.doc(security='apikey')
    @employee_ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_employee()


@employee_ns.route("/<string:emp_code>")
class getEmployee_id(Resource):
    @employee_ns.doc(security='apikey')
    def get(self, emp_code):
        return get_employee(emp_code)
    @employee_ns.doc(security='apikey')
    def delete(self, emp_code):
        return delete_employee(emp_code)

    PUT_DOC_MODEL = employee_ns.model('update_employee', {
        'employee_code': fields.String(example="code01", description='code of the employee'),
        'employee_name': fields.String(example="name", description='name of the employee'),
        'user_account_id': fields.Integer(example="0", description='user account id from user_account table')

    })

    @employee_ns.expect(PUT_DOC_MODEL)
    @employee_ns.doc(security='apikey',params={"emp_code": "enter employee_code"})
    def put(self, emp_code):
        return update_employee(emp_code)


# end points for user_roles <> team
team_ns = Namespace("team", description="team name & id")


@team_ns.route("/")
class getTeam(Resource):
    @team_ns.doc(security='apikey')
    def get(self):
        team_id = None
        return get_team(team_id)

    POST_DOC_MODEL = team_ns.model('add_team', {
        'team_name': fields.String(example="name", description='name of the team')
    })
    @team_ns.doc(security='apikey')
    @team_ns.expect(POST_DOC_MODEL)
    def post(self):
        return create_team()


@team_ns.route("/<string:team_id>")
class getTeam_id(Resource):
    @team_ns.doc(security='apikey')
    def get(self, team_id):
        return get_team(team_id)
    @team_ns.doc(security='apikey')
    def delete(self, team_id):
        return delete_team(team_id)

    PUT_DOC_MODEL = team_ns.model('update_team', {

        'team_name': fields.String(example="name", description='name of the team')
    })

    @team_ns.expect(PUT_DOC_MODEL)
    @team_ns.doc(security='apikey',params={"team_id": "enter team id"})
    def put(self, team_id):
        return update_team(team_id)

# end points for user_roles <> role


role_ns = Namespace("role", description="role name & id")


@role_ns.route("/")
class getRole(Resource):
    @role_ns.doc(security='apikey')
    def get(self):
        role_id = None
        return get_role(role_id)

    POST_DOC_MODEL = role_ns.model('add_role', {
        'role_name': fields.String(example="name", description='role name')
    })

    @role_ns.expect(POST_DOC_MODEL)
    @role_ns.doc(security='apikey')
    def post(self):
        return create_role()


@role_ns.route("/<string:role_id>")
class getRole_id(Resource):
    @role_ns.doc(security='apikey')
    def get(self, role_id):
        return get_role(role_id)
    @role_ns.doc(security='apikey')
    def delete(self, role_id):
        return delete_role(role_id)

    PUT_DOC_MODEL = role_ns.model('update_role', {

        'role_name': fields.String(example="name", description='role name')
    })

    @role_ns.expect(PUT_DOC_MODEL)
    @role_ns.doc(security='apikey',params={"role_id": "enter role id"})
    def put(self, role_id):
        return update_role(role_id)


# end points for user_roles <> team_member
team_member_ns = Namespace("team_member", description="team_member")


@team_member_ns.route("/")
class getTeam_member(Resource):
    POST_DOC_MODEL = team_member_ns.model('add_team_member', {
        'team_id': fields.Integer(example=1, description='id of the team'),
        'role_id': fields.Integer(example=1, description='id of the role'),
        'employee_id': fields.Integer(example=1, description='id of the employee'),
        'active_status': fields.Boolean(example= "true", description='True or False')

    })

    @team_member_ns.expect(POST_DOC_MODEL)
    @team_member_ns.doc(security='apikey')
    def post(self):
        return create_team_member()


@team_member_ns.route("/<int:team_member_id>")
class getTeam_member_id(Resource):
    @team_member_ns.doc(security='apikey')
    def delete(self, team_member_id):
        return delete_team_member(team_member_id)

    PUT_DOC_MODEL = team_member_ns.model('update_team_member', {
         'team_id': fields.Integer(example=1, description='id of the team'),
        'role_id': fields.Integer(example=1, description='id of the role'),
        'employee_id': fields.Integer(example=1, description='id of the employee'),
        'active_status': fields.Boolean(example="true", description='True or False')

    })

    @team_member_ns.expect(PUT_DOC_MODEL)
    @team_member_ns.doc(security='apikey',params={"team_member_id": "enter team-member_id"})
    def put(self, team_member_id):
        return update_team_member(team_member_id)



