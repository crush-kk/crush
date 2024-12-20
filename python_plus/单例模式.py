"""确保一个类只有一个实例"""
class DatabaseConnection:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if  cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
    def connect(self):
        return f"Connecting to databse at {self.host}:{self.port} with {self.username}"
def client():
    db1 = DatabaseConnection("localhost", 3306, "root", "password123")
    db2 = DatabaseConnection("1.1.1.1", 5832, "admin", "admin")
    print(db1 is db2)
client()