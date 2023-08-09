from datetime import timedelta
import os
import time
import logging

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
  
  PERMANENT_SESSION_LIFETIME = timedelta(days=7)
  '''
  错误，表名软件已不能继续运行了
  ERROR 	  40 	发生严重的错误，必须马上处理
  WARNING   30 	应用程序可以容忍这些信息，软件还是在正常工作，不过它们应该被检查及修复，否则将在不久的将来发生问题
  INFO 	  20 	证明事情按预期工作，突出强调应用程序的运行过程
  DEBUG 	  10 	详细信息，只有开发人员调试程序时才需要关注的事情
  NOTSET     0    意指不设置,但是会按照父logger级别来过滤日志(注意：不是最低级别的意思)
  '''

  FileLogLever = logging.INFO  # 写入文件日志级别设置
  ConsoleLogLever = logging.WARNING  # 打印到控制台的日志级别设置
  LoggerLogLever = logging.INFO  # 设置logger日志级别，默认为INFO，设置级别过高会影响日志写入和打印，如，由于在记录日志时没有设置CRITICAL级别的，如果这里设置为CRITICAL，则不会有日志写入文件和打印到控制台

  # 默认log文件信息
  # logFileName = '{}.log'.format(time.strftime('%Y_%m_%d'))
  logFileName = f"{time.strftime('%Y_%m_%d')}.log"
  logFileDir = '.\\logs\\'
  logFilePath = logFileDir + logFileName