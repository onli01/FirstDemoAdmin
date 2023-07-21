from flask_restful import Resource,request,marshal
from flask import jsonify
from common.httpClient import Request


class HttpRequest(Resource):
  def post(self):
    data = request.get_json()
    method = data.get("method")
    if not method:
        return jsonify(dict(code=101, msg="请求方式不能为空"))
    url = data.get("url")
    if not url:
        return jsonify(dict(code=101, msg="请求地址不能为空"))
    body = data.get("body")
    headers = data.get("headers")
    r = Request(url, json=body, headers=headers)
    response = r.request(method)
    return jsonify(dict(code=200, data=response, msg="操作成功"))