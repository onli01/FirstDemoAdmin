from flask_restful import Resource,fields, request,marshal
from common.httpResponse import success_result,params_error
from apps.views.user.userViews import UserView
from common.authToken import AuthToken

# 定义要返回的字段
user_fields = {
            'user_id': fields.Integer(attribute='id'),
            'username': fields.String(),
            'nickname':fields.String(default='--'),
            'email': fields.String(default="--"),
            'img':fields.String(attribute='avatar_image'),
            'reg_time': fields.String(attribute='create_time'),
            'last_time':fields.String(attribute='last_login'),
            'type': fields.Integer(attribute='role'),
            'status':fields.Integer(),
    }

class Register(Resource):

  def post(self):
    data = request.get_json()
    username,password = data.get('username'),data.get('password')
    if not username or not password:
      return params_error(msg='用户名或密码不能为空')
    message = UserView.add_user(username,password)
    if message is not None:
      return params_error(msg=message)
    return success_result(msg='注册成功')
  
  
class Login(Resource):
  def post(self):
    data = request.get_json()
    username,password = data.get('username'),data.get('password')
    if not username or not password:
      return params_error(msg='用户名或密码不能为空')
    result,message = UserView.login(username,password)
    if message is not None:
      return params_error(msg=message)
    user = marshal(result,user_fields)
    token = AuthToken.generate_token(user['user_id'])
    return success_result(msg='登录成功',data=dict(user=user,token=token))
  
  
class GetUser(Resource):
  def get(self):
    data = request.get_json()
    username = data.get('username')
    # username =request.args['username']
    if not username:
      return params_error(msg='用户名不能为空')
    result,message = UserView.get_user(username)
    if message is not None:
      return params_error(msg=message)
    print(result)
    user = marshal(result,user_fields)
    return success_result(data=dict(list=user))
  
  
class UserList(Resource):
  def get(self):
    result,message = UserView.user_list()
    if message is not None:
      return params_error(msg=message)
    print(result)
    user = marshal(result,user_fields)
    # return jsonify(dict(code=200,msg='',data=dict(list=user)))
    return success_result(data=dict(list=user))
  