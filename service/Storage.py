import psycopg2
from entities.Users import *

class Storage:
    user = ""
    password = ""
    host = ""
    port = 0
    database = ""

    connection = None

    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def connect(self):
        self.connection = psycopg2.connect(user=self.user,
                                  password=self.password,
                                  host=self.host,
                                  port=self.port,
                                  database=self.database)

        if(self.connection):
            print("connected on %s@%s:%d" % (self.database, self.host, self.port))
            return True
        
        return false
        

    def close(self):
        if(self.connection):
            self.connection.close()
            print("PostgreSQL connection is closed")            


    def getCursor(self):
        if(self.connection is None):
            print("database is not connected")            

        return self.connection.cursor()           
