from sqlalchemy import DateTime, Enum, Integer, String
from exts import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(Integer, primary_key=True, autoincrement=True, comment='id')
    name = db.Column(String(50), nullable=False, comment='项目名称')
    status = db.Column(Integer, default=1, comment='状态,0:关闭;1:启用')
    owner = db.Column(String(50), comment='所属人')
    description = db.Column(String(200), comment='描述')
    create_time = db.Column(DateTime,default=datetime.now, comment='创建时间')
    update_time = db.Column(DateTime,onupdate=datetime.now,comment='更新时间')
    private = db.Column(Integer,comment='是否私有,0:否;1:是')
    
    def __init__(self, name, owner,private=0,status=1,**kwargs):
      self.name = name
      self.owner = owner
      self.private = private
      self.status = status
      self.description = kwargs['description']