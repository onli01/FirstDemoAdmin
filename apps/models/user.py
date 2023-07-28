from exts import db
from sqlalchemy import DateTime, Integer, String
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
  id  =  db.Column(Integer, primary_key=True, autoincrement=True,comment="用户id")
  username  =  db.Column(String(16),  unique=True,  index=True,comment='用户名')
  nickname  =  db.Column(String(16),  index=True,comment="用户昵称")
  _password  =  db.Column(String(200),comment="用户密码")
  email  =  db.Column(String(64), nullable=True,comment="邮箱")
  role  =  db.Column(Integer,  default=0,  comment="角色,0:普通用户 1:管理员")
  status = db.Column(Integer, nullable=False, default=1,comment="用户状态:1正常,0禁用")
  avatar_image = db.Column(String(100), nullable=True,comment="用户头像")
  create_time = db.Column(DateTime, default=datetime.now,comment="创建时间")
  last_login = db.Column(DateTime, default=datetime.now,comment="最近登录时间")
  update_time = db.Column(DateTime,onupdate=datetime.now,comment="更新时间")

  def  __init__(self, username, password,status=1):
    self.username  =  username
    self.password  =  password
    self.create_time  =  datetime.now()
    self.update_time  =  datetime.now()
    self.role  =  0
    self.status = status
    
    
  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, password):  # 赋值password，则自动加密存储
    self._password = generate_password_hash(password)

  def check_password(self, password):  # 进行密码校验，返回True or False
    # result = check_password_hash(self._password, password)
    return check_password_hash(self._password, password)
  
  


  def  __repr__(self):
    return  '<User  %r>'  %  self.username