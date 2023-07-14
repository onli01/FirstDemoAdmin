from apps.resouses.user.userApi import *
from flask import Blueprint
from flask_restful import Api

userbp = Blueprint('user', __name__, url_prefix='/user')
api = Api(userbp)

api.add_resource(Register,'/register')
api.add_resource(Login,'/login')
api.add_resource(getUser,'/getUser')
