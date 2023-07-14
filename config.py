class Config(object):
  
  #debug调试
  DEBUG = True

  #json编码
  JSON_AS_ASCII = False

  #mysql配置
  MYSQL_HOST = '127.0.0.1'
  MYSQL_PORT = 3306
  MYSQL_USER = 'root'
  MYSQL_PWD = '123456'
  DBNAME = 'apitest'
  DIALECT = 'mysql'
  DRIVER = 'pymysql'

  DB_URI = f'{DIALECT}+{DRIVER}://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{DBNAME}?charset=utf8'

  SQLALCHEMY_DATABASE_URI = DB_URI
  # 数据表的更改追踪，需要消耗额外的资源，不需要可以关闭
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True

  #token加密
  TOKEN_EXPIRE_TIME = 2 * 3600  # token有效时间 2小时
  JWT_SECRET = 'humph'   # 加解密密钥
  JWT_ALGORITHM = 'HS256'  # 加解密算法