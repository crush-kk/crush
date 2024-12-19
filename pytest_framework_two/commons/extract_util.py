import re

import yaml
import  jsonpath

from reload_and_replace_util import reload_and_replace_util

from copy import  deepcopy

from commons.yaml_util import write_yaml


class ExtractUtil:
    def use_extract(self,data: dict):
        return yaml.safe_load(reload_and_replace_util(yaml.safe_dump(data)))
    """
    提取分为两种方式
    1、对于json, jsonpath提取
    2、对于text, re提取
    """
    def extract(self, resp, var_name, attr_name, expr, index):
        copy_resp = deepcopy(resp)
        try:
            copy_resp.json = copy_resp.json()
        except:
            copy_resp.json = {'msg': "response has not such data"}
        #提取数据的地方
        data = getattr(copy_resp, attr_name)
        print(f"-------从这里提取---------{data}")
        # 1.jsonpath提取
        if expr.startswith("$"):
            value =jsonpath.jsonpath(data, expr)
        # 2.re提取
        else:
            value = re.findall(expr, data)
        print(f"-------------进行值的提取-----------------{value}")
        #提取到值了
        if value:

            index = int(index)
            if int(index) == -1:
                print("提取所有的值")
            #     提取所有的值
                write_yaml({var_name: "".join(value)})
            else:
                write_yaml({var_name: value[index]})
