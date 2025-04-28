import sqlite3

class db_wrapper():
    _path = "./data/test.db"
    
    def __init__(self, parameters):
        self.attribute = 1234
        self.client = self.connect()


    def connect(self):
        conn = sqlite3.connect(self._path)
        return conn.cursor()

    def execute(self, sql, parameters=None):
        self.client.execute(sql)
        return self.client.fetchall()


#    @classmethod
#     def f(cls, arg1, arg2): ...