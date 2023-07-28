from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from config import Config
from exts import db
from apps.models.user import User
from apps.models.project import Project
from apps.models.testCase import TestCase
from apps.resouses.user import userbp
from apps.resouses.request import requestbp
from apps.resouses.project import projectbp

app = Flask(__name__)
app.config.from_object(Config)
# 跨域
CORS(app)
'''同步数据库模型
flask db init
flask db migrate
lask db upgrade
'''
#db绑定
db.init_app(app)
migrate = Migrate(app, db)

#注册蓝图
app.register_blueprint(userbp,name="user")
app.register_blueprint(requestbp,name="request")
app.register_blueprint(projectbp,name="project")

if __name__ == '__main__':
    app.run("0.0.0.0", port="8888")
