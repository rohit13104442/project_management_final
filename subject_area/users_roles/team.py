from data.database_connect import db, ma
from flask import request

def get_team(team_id):
    if team_id is None:
        all_data = team.query.all()
        data = teams_schema.jsonify(all_data)
        return data
    else:
        all_data = team.query.filter_by(team_id=team_id).first()
        if all_data is None:
            return "team id code doesn't exist"
        return team_schema.jsonify(all_data)


def create_team():
    team_details = request.json.get

    team_name = team_details("team_name")

    if team_name is None:
        return "team name is not defined"

    all_data = team.query.all()
    for id in all_data:
        if team_name == id.team_name:
            return "team name already registered"

    my_update = team(team_name)
    db.session.add(my_update)
    db.session.commit()
    return {"message": "success"}

def delete_team(team_id):
    all_data = team.query.filter_by(team_id=team_id).first()
    if all_data is None:
        return "team id doesn't exist"

    db.session.delete(all_data)
    db.session.commit()
    return {"message": "success"}


def update_team(team_id):
    data = team.query.filter_by(team_id=team_id).first()

    if data is None:
        return "team id doesn't exist"
    team_details = request.json.get
    team_name = team_details("team_name")

    result = team_schema.dump(data)
    if team_name is None:
        team_name = result["team_name"]
    all_data = team.query.all()
    for id in all_data:
        if team_name == id.team_name:
            return "team name already registered"
    data.team_name = team_name
    db.session.commit()
    return {"message": "success"}
class team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String)

    def __init__(self,  team_name):
        self.team_name = team_name


class teamSchema(ma.Schema):
    class Meta:
        fields = ("team_id", "team_name")


team_schema = teamSchema()
teams_schema = teamSchema(many=True)