import sqlite3

def getItem():
    con = sqlite3.connect("C:/Users/Stud2/Documents/Valeria/lesson4/mydb.db")
    cur = con.cursor()
    cur.execute(''' SELECT Game.Name, Company.Name FROM Game 
                        JOIN Company ON Game.DeveloperID = Company.CompanyId''')
    res = cur.fetchall()
    return res

def getUser(user,psw):
    print (user)
    print (psw)
    con = sqlite3.connect("C:/Users/Stud2/Documents/Valeria/lesson4/mydb.db")
    cur = con.cursor()
    cur.execute(f''' SELECT * FROM User WHERE Login = '{user}' AND Password = '{psw}' ''')
    res = cur.fetchall()
    print(res)
    if res == []:
        return False
    else:
        return True


class Users():
    def __init__(self):
        self.con = sqlite3.connect("C:/Users/Stud2/Documents/Valeria/lesson4/mydb.db")
        self.cur = self.con.cursor()

    def createUser(self,login,password):
        self.cur.execute(f''' INSERT INTO Users ('user','password') VALUES('{login}','{password}') ''')
        self.con.commit()
        print(f"Пользователь {login} успешно создан")

    def authUser(self,login,password):
        self.cur.execute(f''' SELECT * FROM Users WHERE Login = {login} AND Password = {password} ''')
        res = self.cur.fetchall()
        if res == []:
            self.con.commit()
            print (f"Нет такого пользователя")
            return False
        else:
            self.con.commit()
            print (f"Пользователь {login} вошёл в систему")
            return True

class Company():
    def __init__(self):
        self.con = sqlite3.connect("C:/Users/Stud2/Documents/Valeria/lesson4/mydb.db")
        self.cur = self.con.cursor()

    def addCompany(self,name):
        self.cur.execute(f''' SELECT * FROM Company WHERE Name = {name} ''')
        res = self.cur.fetchall()
        if res == []:
            self.cur.execute(f''' SELECT * FROM Company ''')
            res = self.cur.fetchall()
            id = len(res) + 1
            self.cur.execute(f''' INSERT INTO Company ('CompanyId','Name') VALUES('{id}','{name}') ''')
            self.con.commit()
            print(f"Компания {name} успешно добавлена.")
        else:
            print(f"Компания {name} уже есть в базе данных.")

    def editCompany(self,name1,name2):
        self.cur.execute(f''' SELECT * FROM Company WHERE Name = {name1} ''')
        res = self.cur.fetchall()
        if res == []:
            print(f"Компании {name1} нет в системе.")
        else:
            self.cur.execute(f''' UPDATE Company SET Name = '{name2}' WHERE Name = '{name1}' ''')
            self.con.commit()
            print(f"Название компании {name1} изменено на {name2}.")

    def deleteCompany(self,name):
        self.cur.execute(f''' SELECT * FROM Company WHERE Name = {name} ''')
        res = self.cur.fetchall()
        if res == []:
            print(f"Компании {name} нет в системе.")
        else:
            self.cur.execute(f''' DELETE FROM Company WHERE Name = '{name}' ''')
            self.con.commit()
            print(f"Компания {name} удалена из системы.")
    def CompanyList(self):
        self.cur.execute(f''' SELECT Genre.Name FROM Genre''')
        res = self.cur.fetchall()
        return res

class Genre():
    def __init__(self):
        self.con = sqlite3.connect("C:/Users/Stud2/Documents/Valeria/lesson4/mydb.db")
        self.cur = self.con.cursor()

    def addGenre(self,name):
        self.cur.execute(f''' SELECT * FROM Genre WHERE Name = {name} ''')
        res = self.cur.fetchall()
        if res == []:
            self.cur.execute(f''' SELECT * FROM Genre ''')
            res = self.cur.fetchall()
            id = len(res) + 1
            self.cur.execute(f''' INSERT INTO Genre ('GenreId','Name') VALUES('{id}','{name}') ''')
            self.con.commit()
            print(f"Жанр {name} успешно добавлена.")
        else:
            print(f"Жанр {name} уже есть в базе данных.")

    def editGenre(self,name1,name2):
        self.cur.execute(f''' SELECT * FROM Genre WHERE Name = {name1} ''')
        res = self.cur.fetchall()
        if res == []:
            print(f"Жанра {name1} нет в системе.")
        else:
            self.cur.execute(f''' UPDATE Genre SET Name = '{name2}' WHERE Name = '{name1}' ''')
            self.con.commit()
            print(f"Название жанра {name1} изменено на {name2}.")

    def deleteGenre(self,name):
        self.cur.execute(f''' SELECT * FROM Genre WHERE Name = {name} ''')
        res = self.cur.fetchall()
        if res == []:
            print(f"Жанра {name} нет в системе.")
        else:
            self.cur.execute(f''' DELETE FROM Genre WHERE Name = '{name}' ''')
            self.con.commit()
            print(f"Жанр {name} удален из системы.")

    def GenreList(self):
        self.cur.execute(f''' SELECT Genre.Name FROM Genre''')
        res = self.cur.fetchall()
        return res

class Game():
    def __init__(self):
        self.con = sqlite3.connect("C:/Users/Stud2/Documents/Valeria/lesson4/mydb.db")
        self.cur = self.con.cursor()

    def addGame(self,name,company):
        self.cur.execute(f''' SELECT * FROM Genre WHERE Name = {name} ''')
        res = self.cur.fetchall()
        if res == []:
            self.cur.execute(f''' SELECT * FROM Genre ''')
            res = self.cur.fetchall()
            id = len(res) + 1
            self.cur.execute(f''' INSERT INTO Genre ('GenreId','Name') VALUES('{id}','{name}') ''')
            self.con.commit()
            print(f"Жанр {name} успешно добавлена.")
        else:
            print(f"Жанр {name} уже есть в базе данных.")

    def editGenre(self,name1,name2):
        self.cur.execute(f''' SELECT * FROM Genre WHERE Name = {name1} ''')
        res = self.cur.fetchall()
        if res == []:
            print(f"Жанра {name1} нет в системе.")
        else:
            self.cur.execute(f''' UPDATE Genre SET Name = '{name2}' WHERE Name = '{name1}' ''')
            self.con.commit()
            print(f"Название жанра {name1} изменено на {name2}.")

    def deleteGenre(self,name):
        self.cur.execute(f''' SELECT * FROM Genre WHERE Name = {name} ''')
        res = self.cur.fetchall()
        if res == []:
            print(f"Жанра {name} нет в системе.")
        else:
            self.cur.execute(f''' DELETE FROM Genre WHERE Name = '{name}' ''')
            self.con.commit()
            print(f"Жанр {name} удален из системы.")

    def GenreList(self):
        self.cur.execute(f''' SELECT Genre.Name FROM Genre''')
        res = self.cur.fetchall()
        return res