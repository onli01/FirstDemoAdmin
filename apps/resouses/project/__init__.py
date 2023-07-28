from apps.resouses.project.projectApi import *
from flask import Blueprint
from flask_restful import Api

projectbp = Blueprint('user', __name__, url_prefix='/project')
api = Api(projectbp)

api.add_resource(AddProject,'/addProject')
api.add_resource(GetProject,'/getProject')
api.add_resource(ProjectList,'/projectList')