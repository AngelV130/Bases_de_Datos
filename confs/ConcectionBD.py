import mysql.connector
# import pandas
import pandas as pd

class ConnectionBD:
    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.cursor = None
    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        self.cursor = self.connection.cursor()
    def disconnect(self):
        self.connection.close()
        self.cursor.close()
    def execute_query(self, query):
        res = pd.read_sql(query, self.connection)
        return res
    def execute_insert(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount
    def execute_update(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount
    def execute_delete(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount
    


