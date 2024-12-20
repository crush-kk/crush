"""将创造对象 和 使用对象分开"""
from db_configs import db_configs


class DatabaseConnection:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
    def connect(self):
        return f"Connecting to databse at {self.host}:{self.port} with {self.username}"

def connection_factory(db_type):
    return DatabaseConnection(**db_configs[db_type])


def client():
    main_db = connection_factory('main')
    analytics_db = connection_factory('analytics')
    cache_db = connection_factory('cache')

    print(main_db.connect())
    print(analytics_db.connect())
    print(cache_db.connect())
if __name__ == '__main__':
    client()