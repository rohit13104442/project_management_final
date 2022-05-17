
from flask import request, abort
from subject_area.anon_token import  validate_jwt_token

def token_check():
    token = request.headers.get('x-access-token')
    validate_jwt_token(token)
    if validate_jwt_token(token) == False:
        return abort(401, "Unauthorised")



