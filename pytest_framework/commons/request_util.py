import logging

import requests

sess = requests.session()

logger = logging.getLogger(__name__)
class RequestUtil:
    def send_all_requests(self, **kwargs):
        msg = {
            '请求路径':  kwargs['url'],
            '请求方法': kwargs['method'],
            '请求参数': kwargs['data'],
            '请求头': kwargs['headers']
        }
        logger.info(msg)

        return sess.request(**kwargs)
