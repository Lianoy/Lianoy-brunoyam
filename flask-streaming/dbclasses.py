import sqlite3

######################################################################################
##################  GENRES ###########################################################
######################################################################################

def addGenre(name):
    con = sqlite3.connect("H:/Programs/Python/Brunoyam/flask-streaming/streaming.db")
    cur = con.cursor()
    cur.execute(f''' SELECT * FROM Genre WHERE Name = '{name}' ''')
    res = cur.fetchall()
    if res == []:
        # self.cur.execute(f''' SELECT * FROM Genre ''')
        # res = self.cur.fetchall()
        # id = len(res) + 1
        # self.cur.execute(f''' INSERT INTO Genre ('GenreId','Name') VALUES('{id}','{name}') ''')
        cur = con.cursor()
        cur.execute(f''' INSERT INTO Genre ('Name') VALUES ('{name}') ''')
        con.commit()
        print(f"Жанр {name} успешно добавлен.")
        return True
    else:
        print(f"Жанр {name} уже есть в базе данных.")
        return False

def editGenre(name1,name2):
    con = sqlite3.connect("streaming.db")
    cur = con.cursor()
    cur.execute(f''' SELECT * FROM Genre WHERE Name = {name1} ''')
    res = cur.fetchall()
    if res == []:
        print(f"Жанра {name1} нет в системе.")
    else:
        cur.execute(f''' UPDATE Genre SET Name = '{name2}' WHERE Name = '{name1}' ''')
        con.commit()
        print(f"Название жанра {name1} изменено на {name2}.")

def deleteGenre(name):
    con = sqlite3.connect("streaming.db")
    cur = con.cursor()
    cur.execute(f''' SELECT * FROM Genre WHERE Name = {name} ''')
    res = cur.fetchall()
    if res == []:
        print(f"Жанра {name} нет в системе.")
    else:
        cur.execute(f''' DELETE FROM Genre WHERE Name = '{name}' ''')
        con.commit()
        print(f"Жанр {name} удален из системы.")

def GenreList():
    con = sqlite3.connect("H:/Programs/Python/Brunoyam/flask-streaming/streaming.db")
    cur = con.cursor()
    cur.execute(f''' SELECT Genre.Name FROM Genre''')
    res = cur.fetchall()
    res1 = []
    for i in res:
        res1.append(i[0])
    res1.sort()
    return res1