import time

from flask_restx import Api
from flask import Flask , request

from subject_area.endpoints.user_roles_endpoints import user_account_ns,employee_ns,team_ns, role_ns, team_member_ns
from subject_area.endpoints.projects_endpoints import project_ns, project_manager_ns, client_partner_ns, on_project_ns, status_ns
from subject_area.endpoints.task_activity_endpoints import task_ns, activity_ns, assigned_ns
from subject_area.progress_table import progress_table_ns
from subject_area.anon_token import anon_token_ns
from data.database_connect import app
from subject_area.endpoints.validators import token_check

# def before_request():
#     token_check()


def configure_endpoints(app):
    authorizations= {
        'apikey':{
            'type': 'apiKey',
            'in': 'header',
            'name': 'x-access-token',

        }
    }
    restx_api = Api(
        title= 'Crunum API',
        version= "1.0",
        description="API documentation for crunum app apis",
        authorizations=authorizations
    )

# route import from user_roles

    restx_api.add_namespace(user_account_ns)
    restx_api.add_namespace(employee_ns)
    restx_api.add_namespace(team_ns)
    restx_api.add_namespace(role_ns)
    restx_api.add_namespace(team_member_ns)

    # route import from projects
    restx_api.add_namespace(project_ns)
    restx_api.add_namespace(project_manager_ns)
    restx_api.add_namespace(client_partner_ns)
    restx_api.add_namespace(on_project_ns)
    restx_api.add_namespace(status_ns)

    # route import from task_activity
    restx_api.add_namespace(task_ns)
    restx_api.add_namespace(activity_ns)
    restx_api.add_namespace(assigned_ns)

    # route import from progress_table
    restx_api.add_namespace(progress_table_ns)


    # route import from anon_token
    restx_api.add_namespace(anon_token_ns)


    restx_api.init_app(app)




    return app

def init_app():

    app.route("/")

    configure_endpoints(app)
    return app





if __name__== "__main__":
    app = init_app()

    app.run(host='0.0.0.0',debug=True,port=5555)