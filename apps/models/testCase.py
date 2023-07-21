from sqlalchemy import DATETIME, TEXT, Integer, String
from exts import db
from datetime import datetime

class TestCase(db.Model):
    __tablename__ = "test_case"
    id = db.Column(Integer, primary_key=True, autoincrement=True, comment='id')
    name = db.Column(String(32), unique=True, index=True,comment='用例名称')
    request_type = db.Column(Integer, default=1, comment="请求类型 1: http 2: grpc 3: dubbo")
    url = db.Column(TEXT, nullable=False, comment="请求url")
    request_method = db.Column(String(12), nullable=True, comment="请求方式, 如果非http可为空")
    request_header = db.Column(TEXT, comment="请求头，可为空")
    params = db.Column(TEXT, comment='请求params')
    body = db.Column(TEXT, comment='请求body')
    project_id = db.Column(Integer, comment="所属项目")
    tag = db.Column(String(64), comment="用例标签")
    status = db.Column(Integer, comment="用例状态: 1: 待完成 2: 暂时关闭 3: 正常运作")
    expected = db.Column(TEXT, comment="预期结果, 支持el表达式", nullable=False)
    create_time = db.Column(DATETIME, nullable=False)
    update_time = db.Column(DATETIME, nullable=False)
   

    def __init__(self, name, request_type, url, project_id, tag, status, expected, create_user, request_header=None,
                 request_method=None):
        self.name = name
        self.request_type = request_type
        self.url = url
        self.project_id = project_id
        self.tag = tag
        self.status = status
        self.expected = expected
        self.create_user = create_user
        self.update_user = create_user
        self.request_header = request_header
        self.request_method = request_method
        self.create_time = datetime.now()
        self.update_time = datetime.now()