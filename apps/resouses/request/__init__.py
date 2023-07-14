from apps.resouses.request.requestApi import *
from flask import Blueprint
from flask_restful import Api

requestbp = Blueprint('user', __name__, url_prefix='/request')
api = Api(requestbp)

api.add_resource(HttpRequest,'/sendRequest')
