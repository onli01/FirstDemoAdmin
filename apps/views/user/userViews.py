from datetime import datetime
from apps.models.user import User
from exts import db


class UserView(object):
  
  @staticmethod
  def add_user(username,password):
    """
    :param username: 用户名
    :param password: 密码
    :return:
    """
    try:
      user = User.query.filter_by(username = username).first()
      if user is not None:
        raise Exception('用户名已存在')
      user= User(username,password)
      db.session.add(user)
      db.session.commit()
    except Exception as e:
      # log.info(f"用户注册失败：{str(e)}")
      return str(e)
    return None
  
  @staticmethod
  def login(username,password):
    try:
      user = User.query.filter_by(username = username).first()
      if user and user.check_password(password):
        user.last_login = datetime.now()
        db.session.commit()
        return user,None
        
      else:
        return None,'用户名或密码错误'
    except Exception as e:
      #log.info(f'用户{username}登录失败:{str(e)}')
      return None,str(e)
    
  @staticmethod 
  def get_user(username):
    try:
      user = User.query.filter_by(username = username).first()
      if user :
        return user,None 
      else:
        return None,'用户名不存在！'
    except Exception as e:
      #log.info(f'用户{username}登录失败:{str(e)}')
      return None,str(e)