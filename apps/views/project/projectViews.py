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