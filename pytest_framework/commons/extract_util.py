import re
import  jsonpath
from copy import deepcopy

import yaml

from commons.request_util import logger
from commons.load_and_replace import load_and_replace
from commons.yaml_util import  write_yaml
# qww
class ExtractUtil:
    def extract(self, resp, var_name, attr_name, expr, index):
        """
        解析并提取测试用例中的extract字段
        :param resp: 响应数据
        :param var_name: 中间变量的名字
        :param attr_name: 从哪提取
        :param expr: 匹配的表达式
        :param index: 提取的索引
        :return: 返回提取的值
        """
        # 提取分为两种方式 1: 在html中用re提取, 2:在json中用Jsonpath提取
        copy_resp = deepcopy(resp)
        # 因为json是一个方法先把json存储为copy_resp的属性值，方便反射
        try:
            copy_resp.json = copy_resp.json()
        except Exception:
            copy_resp.json = {"msg": "response has not json data"}
        data = getattr(copy_resp, attr_name)
        # 开始判断方式并提起
        if expr.startswith('$'):
            extract_list = jsonpath.jsonpath(data, expr)
        else:
            extract_list = re.findall(expr, data)
        if extract_list:
                write_yaml({var_name: extract_list[index]})
                logger.info(f"写入了中间变量{var_name}值{extract_list[index]}")

    def use_extract(self, data:dict):
        """进行加载替换，并判断是否需要使用extract的值"""
        return yaml.safe_load(load_and_replace(yaml.safe_dump(data)))