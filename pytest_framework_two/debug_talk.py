from commons.config_util import read_config
from yaml_util import read_yaml


class DebugTalk:
    def env(self,key):
        return read_config()[key]
    def add(self, a, b):
        return a+b
    def password(self):
        return 12345678
    def get_value_by_key(self,key, is_use_digit):
        return  read_yaml(key) if not is_use_digit else int(read_yaml(key))
if __name__ == '__main__':
    print(DebugTalk().get_value_by_key('goods_id'))

