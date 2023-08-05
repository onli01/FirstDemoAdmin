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
            'create_time': fields.String(),
            'last_login':fields.String(),
            'type': fields.Integer(attribute='role'),
            'status':fields.Integer(),
    }

class Register(Resource):

  def post(self):
    data = request.get_json()
    username,password = data.get('username'),data.get('password')
    if not username or not password:
      return params_error(msg='用户名或密码不能为空')
    message = UserView.addUser(username,password)
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
  
  
class OutLogin(Resource):
  def post(self):
    message = UserView.outLogin()
    return success_result(msg=message)
  
  
class GetUserByName(Resource):
  def get(self):
    data = request.get_json()
    username = data.get('username')
    # username =request.args['username']
    if not username:
      result,message = UserView.getUserAll()
    else:
      result,message = UserView.getUserByName(username)
    if message is not None:
      return params_error(msg=message)
    print(result)
    user = marshal(result,user_fields)
    return success_result(data=dict(list=user))
  
  
class GetUserAll(Resource):
  def get(self):
    result,message = UserView.getUserAll()
    if message is not None:
      return params_error(msg=message)
    print(result)
    user = marshal(result,user_fields)
    # return jsonify(dict(code=200,msg='',data=dict(list=user)))
    return success_result(data=dict(list=user))
  