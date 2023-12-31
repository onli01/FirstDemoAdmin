from flask import jsonify


class HttpCode(object):
    ok = 200
    params_error = 400
    un_auth_error = 401
    server_error = 500


def restful_result(code, msg='', data=None):
    # return jsonify({"code": code, "msg": msg, "data": data or {}})
    return jsonify(dict(code=code,msg=msg,data=data))


def success_result(msg="", data=None):
    """
    正确返回
    :return:
    """
    return restful_result(code=HttpCode.ok, msg=msg, data=data)


def params_error(msg=""):
    """
    参数错误
    :return:
    """
    return restful_result(HttpCode.params_error, msg=msg)


def unauth_error(msg=""):
    """
    没有权限
    :return:
    """
    return restful_result(HttpCode.un_auth_error, msg=msg)


def server_error(msg=""):
    """
    服务器错误
    :return:
    """
    return restful_result(HttpCode.server_error, msg=msg)
