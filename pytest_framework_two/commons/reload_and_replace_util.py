import  re
from debug_talk import DebugTalk
dg = DebugTalk()
def reload_and_replace_util(data_str: str):
    """
    进行热加载和替换
    :param data_str:
    :return:
    """
    #定义规则匹配测试用例中的函数
    regex =r"\$\{(.*?)\((.*?)\)\}"
    #解包得到方法名和参数
    for func, params in re.findall(regex, data_str):
        #如果没有参数，直接调用
        old_value = f"${{{func}({params})}}"
        if not params:
            value = getattr(dg, func)()
        #如果有参数
        else:
            value =  getattr(dg, func)(*params.split(","))
        if isinstance(value, str) and value.isdigit():
            value = f"'{value}'"
        data_str = data_str.replace(old_value, str(value))
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
          "name": "${add(1,2)}",
          "password": "${password()}"
        }
      }
    }"""
    print(reload_and_replace_util(json))