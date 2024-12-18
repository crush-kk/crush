import  yaml


def write_yaml(data):
    with open("extract.yaml", 'a+', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
def clean_yaml():
    with open("extract.yaml", 'w', encoding='utf-8') as f:
        pass
def read_yaml():
    pass