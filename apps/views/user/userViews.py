from datetime import datetime
from apps.models.user import User
from exts import db
from common.handleLog import Logger

log = Logger(logger='userView',loglevel=1).getlog()

class UserView(object):
  
  @staticmethod
  async def addUser(username,password):
    """
    :param username: 用户名
    :param password: 密码
    :return:
    """
    try:
      user =await User.query.filter_by(username = username).all()
      if user is not None:
        raise Exception('用户名已存在')
      user= User(username,password)
      db.session.add(user)
      db.session.commit()
    except Exception as e:
      log.info(f"用户{username}注册失败：{str(e)}")
      return str(e)
    return None
  
  @staticmethod
  async def login(username,password):
    try:
      user =await User.query.filter_by(username = username).first()
      if user and user.check_password(password):
        user.last_login = datetime.now()
        db.session.commit()
        return user,None
        
      else:
        return None,'用户名或密码错误'
    except Exception as e:
      log.info(f'用户{username}登录失败:{str(e)}')
      return None,str(e)
    
    
  @staticmethod
  async def outLogin():
    return '退出成功'

    
  @staticmethod 
  async def getUserByName(username):
    try:
      user =await User.query.filter_by(username = username).all()
      if user :
        return user,None 
      else:
        return None,'用户名不存在！'
    except Exception as e:
      log.info(f'用户{username}查询失败:{str(e)}')
      return None,str(e)
    
  @staticmethod 
  async def getUserAll():
    try:
      userList =await User.query.filter_by(status = 1).all()
      if userList :
        return userList,None 
      else:
        return None,'暂无数据！'
    except Exception as e:
      log.info(f'用户列表获取失败:{str(e)}')
      return None,str(e)