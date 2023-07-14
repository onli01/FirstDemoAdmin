import jwt,time
from config import Config



class AuthToken(object):

  @staticmethod
  def generate_token(user_id: int)->str:
    """根据用户id生成token"""
    payload = {'user_id': user_id, 'exp': int(time.time()) + Config.TOKEN_EXPIRE_TIME}
    token = jwt.encode(payload, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)
    print(token)
    return token


  @staticmethod
  def verify_token(user_id: int, token: str)->bool:
    """验证用户token"""
    payload = {'user_id': user_id}
    try:
        _payload = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM])
    except jwt.PyJWTError:
        print('token解析失败')
        return False
    else:
        print(_payload)
        exp = int(_payload.pop('exp'))
        # print(time.time(),exp)
        if time.time() > exp:
            print('token已过期')
            return False
        return payload == _payload