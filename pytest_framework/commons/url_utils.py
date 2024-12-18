from  iniconfig import IniConfig
def read_url():
    ini = IniConfig(r'./pytest.ini')
    if 'base_url' in ini:
        return dict(ini['base_url'].items())
    return {}
