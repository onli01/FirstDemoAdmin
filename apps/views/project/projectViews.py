from apps.models.project import Project
from exts import db
from common.handleLog import Logger

log = Logger(logger='projectView',loglevel=1).getlog()

class ProjectView(object):
  
  
  @staticmethod
  def addProject(name,owner,**kwargs):
    """
    :param name: 项目名
    :param owner: 所属人
    :return:
    """
    try:
      user = Project.query.filter_by(name = name).first()
      if user is not None:
        raise Exception('项目名称已存在')
      project= Project(name,owner,private=0,status=1,**kwargs)
      db.session.add(project)
      db.session.commit()
    except Exception as e:
      log.info(f"添加失败：{str(e)}")
      return str(e)
    return None
  
  @staticmethod 
  def getProjectByName(name):
    try:
      project = Project.query.filter_by(name = name).all()
      if project :
        return project,None 
      else:
        return None,'项目不存在！'
    except Exception as e:
      log.info(f'查询项目{name}失败:{str(e)}')
      return None,str(e)
    
    
  @staticmethod 
  def getProjectAll():
    try:
      project = Project.query.filter_by(status=1).all()
      return project,None 
    except Exception as e:
      log.info(f'项目列表获取失败:{str(e)}')
      return None,str(e)