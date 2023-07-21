import datetime
import requests


class Request(object):

    def __init__(self, url, session=False, **kwargs) -> None:
        self.url = url
        self.session = session
        self.kwargs = kwargs
        if self.session:
            self.client = requests.session()
            return
        self.client = requests

    def request(self, method: str):
        statusCode = 0
        elapsed = "-1ms"
        try:
            if method.upper() == "GET":
                print(self.kwargs)
                response = self.client.get(self.url, **self.kwargs)
                
            elif method.upper() == "POST":
               
                response = self.client.post(self.url, **self.kwargs)
                # print(response.text)
            else:
                response = self.client.request(method, self.url, **self.kwargs)
            statusCode = response.status_code
            if statusCode != 200:
                return Request.response(False, statusCode)
            elapsed = Request.get_elapsed(response.elapsed)
            cookies = response.cookies
            data = self.get_reponse(response)
            return Request.response(status=True,
                                    status_code=200,
                                    response=data,
                                    response_header=response.headers,
                                    request_header=response.request.headers,
                                    elapsed=elapsed,
                                    cookies=cookies)
        except Exception as e:
            return Request.response(False,
                                    statusCode,
                                    msg=str(e),
                                    elapsed=elapsed)
            
    def get_reponse(self,response):
      try:
        return response.json()
      except Exception:
        return response.text

    @staticmethod
    def get_elapsed(timer: datetime.timedelta):
        if timer.seconds > 0:
            return f"{timer.seconds}.{timer.microseconds // 1000}s"
        return f"{timer.microseconds // 100}ms"

    @staticmethod
    def response(status,
                 status_code=200,
                 response=None,
                 response_header=None,
                 request_header=None,
                 elapsed=None,
                 msg="success",
                 cookies=None):
        # print(request_header)
        # print(response_header)
        # request_header = {k: v for k, v in request_header.items()}
        request_header = dict(request_header.items()) if request_header is not None else {}
        # response_header = {k: v for k, v in response_header.items()}
        response_header = dict(response_header.items()) if response_header is not None else {}
        cookies = dict(cookies) if cookies is not None else {}
        
        return {
            "status": status,
            "response": response,
            "status_code": status_code,
            "response_header": response_header,
            "request_header": request_header,
            "msg": msg,
            "elapsed": elapsed,
            "cookies":cookies,
        }

    def get(self):
        return self.request("GET")

    def post(self):
        return self.request("POST")
