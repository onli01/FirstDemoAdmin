from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import fields

class User(db.Model):
  id  =  db.Column(db.INT,  primary_key=True)
  username  =  db.Column(db.String(16),  unique=True,  index=True)
  nickname  =  db.Column(db.String(16),  index=True)
  _password  =  db.Column(db.String(200))
  email  =  db.Column(db.String(64), nullable=True)
  role  =  db.Column(db.INT,  default=0,  comment="0:  普通用户  1:  组长  2:  超级管理员")
  create_time  =  db.Column(db.DATETIME,  nullable=False)
  updated_time  =  db.Column(db.DATETIME,  nullable=False)
  last_login  =  db.Column(db.DATETIME)

  def  __init__(self, username,  password):
    self.username  =  username
    self.password  =  password
    self.create_time  =  datetime.now()
    self.updated_time  =  datetime.now()
    self.role  =  0
    
    
  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, password):  # 赋值password，则自动加密存储
    self._password = generate_password_hash(password)

  def check_password(self, password):  # 进行密码校验，返回True or False
    result = check_password_hash(self._password, password)
    return result
  
  
  # 定义要返回的字段
  user_fields = {
            'user_id': fields.Integer(attribute='id'),
            'username': fields.String(),
            'nickname':fields.String(default='--'),
            'email': fields.String(default="--"),
            # 'img':fields.String(attribute='avatar_image'),
            'reg_time': fields.String(attribute='create_time'),
            'last_time':fields.String(attribute='last_login'),
            'type': fields.Integer(attribute='role')
    }

  def  __repr__(self):
    return  '<User  %r>'  %  self.username