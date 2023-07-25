from flask_restful import Resource,request,marshal
from flask import jsonify
from apps.views.project.projectViews import ProjectView

class AddProject(Resource):

  def post(self):
    data = request.get_json()
    name,owner = data.get('name'),data.get('owner')
    if not name or not owner:
      return jsonify(dict(code=101,msg='项目名称或所属人不能为空'))
    result = ProjectView.add_project(name,owner)
    if result is not None:
      return jsonify(dict(code=101,msg=result))
    return jsonify(dict(code=200,msg='添加成功'))