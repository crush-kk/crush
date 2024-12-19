from iniconfig import  IniConfig

def read_config():
    #加载配置文件
    config = IniConfig("pytest.ini")
    #得到[]对应的内容，以字典的形式返回
    if 'base_url' in config:
        return dict(config['base_url'].items())
    else:
        return{}

