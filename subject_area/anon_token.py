from data.database_connect import db, ma, app


import datetime
from flask_restx import  Resource, Namespace
import jwt
app.config['SECRET_KEY']= 'crunum'


class anon_token(db.Model):
    anon_token_id = db.Column(db.Integer, primary_key = True)
    anon_token = db.Column(db.TEXT)

    def __init__(self,anon_token):
        self.anon_token = anon_token

class anon_tokenSchema(ma.Schema) :
    class Meta:
        fields = ("anon_token_id", "anon_token")
anon_token_schema = anon_tokenSchema()
anons_token_schema = anon_tokenSchema(many=True)


def generate_token():
    token = jwt.encode({'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=100)},app.config['SECRET_KEY'])
    anonymous_token= token
    my_update = anon_token(anonymous_token)
    db.session.add(my_update)
    db.session.commit()
    return token

def validate_jwt_token(token):
    # try:
    #     data = anon_token.query.filter_by(anon_token=token).first()
    #     data = jwt.decode(token,app.config['SECRET_KEY'],algorithms='HS256')
    #     return True
    # except : return False
    data = anon_token.query.filter_by(anon_token=token).first()

    if data is not None:
        return True
    # try:
    #     data = jwt.decode(token,app.config['SECRET_KEY'],algorithms='HS256')
    #     return True
    # except : return False

    else: return False


anon_token_ns = Namespace("anonymous_token")
@anon_token_ns.route("/")



class get_token(Resource):
    def get(self):
        return generate_token()




