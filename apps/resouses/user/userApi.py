from flask_restful import Resource,request,marshal
from flask import jsonify
from apps.views.user.userViews import UserView
from common.authToken import AuthToken

class Register(Resource):

  def post(self):
    data = request.get_json()
    username,password = data.get('username'),data.get('password')
    if not username or not password:
      return jsonify(dict(code=101,msg='用户名或密码不能为空'))
    result = UserView.add_user(username,password)
    if result is not None:
      return jsonify(dict(code=101,msg=result))
    return jsonify(dict(code=200,msg='注册成功'))
  
  
class Login(Resource):
  def post(self):
    data = request.get_json()
    username,password = data.get('username'),data.get('password')
    if not username or not password:
      return jsonify(dict(code=101,msg='用户名或密码不能为空'))
    user,result = UserView.login(username,password)
    if result is not None:
      return jsonify(dict(code=101,msg=result))
    user = marshal(user,user.user_fields)
    token = AuthToken.generate_token(user['user_id'])
    return jsonify(dict(code=200,msg='登录成功',data=user,token=token))
  
  
class getUser(Resource):
  def get(self):
    # data = request.get_json()
    # username = data.get('username')
    username =request.args['username']
    if not username:
      return jsonify(dict(code=101,msg='用户名不能为空'))
    user,result = UserView.get_user(username)
    if result is not None:
      return jsonify(dict(code=101,msg=result))
    user = marshal(user,user.user_fields)
    return jsonify(dict(code=200,msg='',data=dict(user=user)))