import psycopg2


class User:
    Id = 0
    Name = ""
    Email = ""
    Spaces = 1
    Targets = []

    def __init__(self, id, name, email, spaces, targets):
        self.Id = id
        self.Name = name
        self.Email = email
        self.Sapces = spaces
        self.Targets = targets


class UserStorage:
    def save(cursor, user):
        try:
            query = """ INSERT INTO Users (UserID, Name, Email, Spaces) VALUES (%s, %s, %s, %d)"""
            data = (self.Id, self.Name, self.Email, self.Spaces)
            cursor.execute(query, data)

            connection.commit()
            count = cursor.rowcount
            print("Records affected on Users.Save: %d" % (count))

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into Users table", error)

    def load(cursor):
        ret = []

        try:
            query = """
SELECT
    UserID,
    Name,
    Email,
    Spaces,
    Targets
FROM 
    USERS
ORDER BY
    UserID;
"""
            cursor.execute(query)
            data = cursor.fetchall()

            for row in data:
                ret.append(User(row[0], row[1], row[2], row[3], row[4]))

            return ret
        except (Exception, psycopg2.Error) as error:
            print("Failed to try read Users data: ", error)
