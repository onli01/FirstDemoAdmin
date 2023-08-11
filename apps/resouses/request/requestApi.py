from flask_restful import Resource,request
from common.httpResponse import success_result,params_error
from common.httpClient import Request
from common.handleLog import Logger

log = Logger(logger='requestApi',loglevel=1).getlog()


class HttpRequest(Resource):
  async def post(self):
    data = request.get_json()
    log.info(f'参数：{data}')
    method = data.get("method")
    if not method:
        return params_error(msg="请求方式不能为空")
    url = data.get("url")
    if not url:
        return params_error( msg="请求地址不能为空")
    body = data.get("body")
    headers = data.get("headers")
    r = Request(url, json=body, headers=headers)
    response =await r.request(method)
    return success_result(data=response, msg="操作成功")