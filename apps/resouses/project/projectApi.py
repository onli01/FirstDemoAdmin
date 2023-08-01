from flask_restful import Resource,request,fields,marshal
from common.httpResponse import success_result,params_error
from apps.views.project.projectViews import ProjectView

project_field={
  'id':fields.Integer(),
  'name':fields.String(),
  'owner':fields.String(),
  'status':fields.Integer(),
  'description':fields.String(),
  'create_time':fields.String(),
  'update_time':fields.String(),
  'private':fields.Integer()
}

class AddProject(Resource):

  def post(self):
    data = request.get_json()
    name,owner = data.get('name'),data.get('owner')
    if not name or not owner:
      return params_error(msg='项目名称或所属人不能为空')
    message = ProjectView.addProject(**data)
    if message is not None:
      return params_error(msg=message)
    return success_result(msg='添加成功')
  

class GetProjectByName(Resource):

  def get(self):
    # data = request.get_json()
    # name = data.get('name')
    name = request.args['name']
    print(name)
    if not name:
      result,message = ProjectView.getProjectAll()
    else:
      result,message = ProjectView.getProjectByName(name)
    if message is not None:
      return params_error(msg=message)
    project = marshal(result,project_field)
    return success_result(data=dict(list=project))
  
class GetProjectAll(Resource):

  def get(self):
    result,message = ProjectView.getProjectAll()
    if message is not None:
      return params_error(msg=message)
    project = marshal(result,project_field)
    return success_result(data=dict(list=project))