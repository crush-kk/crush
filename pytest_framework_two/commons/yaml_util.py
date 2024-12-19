import yaml

# 中间变量写入yaml
def write_yaml(data):
    with open("./extract.yaml", "a+", encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
def clean_yaml():
    with open("./extract.yaml", 'w') as f:
        pass
def read_yaml(key):
    with open("./extract.yaml") as f:
        dict_extract = yaml.safe_load(f)
        return dict_extract[key]

