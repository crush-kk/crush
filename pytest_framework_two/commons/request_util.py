from requests import session

req = session().request
class RequestUtil:
    # 处理所有请求
    def send_all_requests(self,**kwargs):
        print('*'*1000)
        print(kwargs['data'])
        resp = req(**kwargs)
        resp.encoding ='utf-8'
        return  resp

