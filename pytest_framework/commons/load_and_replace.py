import re

from debug_talk import DebugTalk

def load_and_replace(data_str: str):
    """
    热加载和替换 yaml中的函数
    :param data_str: 替换前的字符串
    :return: 替换后的内容
    """
    reg = r"\$\{(.*?)\((.*?)\)\}"
    function_list =   re.findall(reg, data_str)
    for function in function_list:
        func_name, func_params = function
        old_value = "${" + func_name + "(" + func_params + ")}"
        if not func_params:
            #无参类型
           return_value =  getattr(DebugTalk(), func_name)()
        else:
            #有参数
            return_value = getattr(DebugTalk(), func_name)(*func_params.split(","))
        if isinstance(return_value, str) and return_value.isdigit():
            return_value = "'" + return_value + "'"
        data_str = data_str.replace(old_value, str(return_value))
    return data_str

if __name__ == '__main__':
    json = """{
  "feature": "ecshop商城",
  "story": "登录端口",
  "title": "验证ecshop登录接口登录成功",
  "request": {
    "method": "post",
    "url": "${env(web_url)}?url=/user/signin",
    "data": {
      "name": "${add(a,b)}",
      "password": "${password()}"
    }
  }
}"""
    print(load_and_replace(json))