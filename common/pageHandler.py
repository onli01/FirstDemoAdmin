from flask import request

PAGE=1
SIZE=10

class PageHandler():
  
  @staticmethod
  def pageInfo():
    page = request.args.get("page")
    size =request.args.get('size')
    if page is None or not page.isdigit():
      page = PAGE
    if size is None or not size.isdigit():
      size = SIZE
    return int(page),int(size)