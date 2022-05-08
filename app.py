from flask_restx import Api
from data.database_connect import app
from subject_area.endpoints.user_roles_endpoints import user_account_ns,employee_ns,team_ns, role_ns, team_member_ns
from subject_area.endpoints.projects_endpoints import project_ns, project_manager_ns, client_partner_ns, on_project_ns
from subject_area.endpoints.task_activity_endpoints import task_ns, activity_ns, assigned_ns
api = Api(app,title="Crunum API", version='1',description='API documentation for crunum app apis')

# route import from user_roles
api.add_namespace(user_account_ns)
api.add_namespace(employee_ns)
api.add_namespace(team_ns)
api.add_namespace(role_ns)
api.add_namespace(team_member_ns)

# route import from projects
api.add_namespace(project_ns)
api.add_namespace(project_manager_ns)
api.add_namespace(client_partner_ns)
api.add_namespace(on_project_ns)

# route import from task_activity
api.add_namespace(task_ns)
api.add_namespace(activity_ns)
api.add_namespace(assigned_ns)

if __name__== "__main__":
    app.run(host='0.0.0.0',debug=True,port=5555)