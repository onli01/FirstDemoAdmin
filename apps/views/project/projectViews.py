from apps.models.project import Project
from exts import db

class ProjectView(object):
  
  
  @staticmethod
  def add_project(name,owner):
    """
    :param name: 项目名
    :param owner: 所属人
    :return:
    """
    try:
      user = Project.query.filter_by(name = name).first()
      if user is not None:
        raise Exception('项目名称已存在')
      project= Project(name,owner)
      db.session.add(project)
      db.session.commit()
    except Exception as e:
      # log.info(f"添加失败：{str(e)}")
      return str(e)
    return None
  
  @staticmethod 
  def get_project(name):
    try:
      project = Project.query.filter_by(name = name).first()
      if project :
        return project,None 
      else:
        return None,'项目不存在！'
    except Exception as e:
      #log.info(f'用户{username}登录失败:{str(e)}')
      return None,str(e)
    
    
  @staticmethod 
  def project_list():
    try:
      project = Project.query.filter_by(status=1).all()
      if project :
        return project,None 
      else:
        return None,'暂无数据！'
    except Exception as e:
      #log.info(f'用户{username}登录失败:{str(e)}')
      return None,str(e)