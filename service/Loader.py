from entities.Users import *
from service.Storage import *

def ShowUsers():
    db = Storage("bianca", "b1@nc@", "localhost", 5432, "garagedraw")
    db.connect()
    cursor = db.getCursor()

    if(cursor is None):
        print("Fail to try get cursor")
    
    data = UserStorage.load(cursor)
    db.close()
    print("user: %s" % (data))
    

    return data