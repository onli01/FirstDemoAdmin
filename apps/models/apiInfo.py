from sqlalchemy import TEXT, DateTime, Integer, String
from exts import db
from datetime import datetime

class ApiInfo(db.Model):
    __tablename__ = "api_info"
    id = db.Column(Integer, primary_key=True, autoincrement=True, comment='id')
    name = db.Column(String(32), unique=True, index=True,comment='接口名称')
    request_type = db.Column(Integer, default=1, comment="请求类型 1: http 2: grpc 3: dubbo")
    url = db.Column(TEXT, nullable=False, comment="请求url")
    request_method = db.Column(String(12), nullable=True, comment="请求方式, 如果非http可为空")
    params = db.Column(TEXT, comment='请求params示例')
    body = db.Column(TEXT, comment='请求body示例')
    project_id = db.Column(Integer, comment="所属项目")
    tag = db.Column(String(64), comment="接口标签")
    auth = db.Column(String(32),comment='开发者')
    status = db.Column(Integer, comment="接口状态")
    expected = db.Column(TEXT, nullable=False, comment="返回字段示例")
    create_time = db.Column(DateTime, nullable=False,comment='创建时间')
    update_time = db.Column(DateTime, nullable=False,comment='更新时间')
   

    def __init__(self, name, request_type, url,params,body, project_id, tag, status, expected, request_header=None,
                 request_method=None):
        self.name = name
        self.request_type = request_type
        self.url = url
        self.params = params
        self.body = body
        self.project_id = project_id
        self.tag = tag
        self.status = status
        self.expected = expected
        self.request_header = request_header
        self.request_method = request_method
        self.create_time = datetime.now()
        self.update_time = datetime.now()