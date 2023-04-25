#INSERT INTO `adatok`(`név`, `kor`, `magasság`) VALUES ('Sanyi', '23', '150');

#SELECT * FROM `adatok` WHERE 1


import pymysql

defaults={
    "DB_NAME": "11b",
    "DB_HOST": "127.0.0.1",
    "DB_PORT": 3306,
    "DB_USER": "11b_user",
    "DB_PASSWD": "11b_user",
    "DB_TABLE": "adatok"
}
def connectDB(_host, _port, _user, _password, _database):
    return pymysql.connect(
            host=_host,
            port=_port,
            user=_user,
            password=_password,
            database=_database
        )

def selectDB(_tablename, _oszlopnevek='*', _feltetel="1"):
    conn=connectDB(
        _host=defaults["DB_HOST"],
        _port=defaults["DB_PORT"],
        _user=defaults["DB_USER"],
        _password=defaults["DB_PASSWD"],
        _database=defaults["DB_NAME"]
    )
    cursor=conn.cursor()
    sql=f"SELECT {_oszlopnevek} FROM `{_tablename}` WHERE {_feltetel}"
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.close()
    return rows

def doItDB(sql):
    conn=connectDB(
        _host=defaults["DB_HOST"],
        _port=defaults["DB_PORT"],
        _user=defaults["DB_USER"],
        _password=defaults["DB_PASSWD"],
        _database=defaults["DB_NAME"]
    )
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insertDB(nev, kor, magassag):
    sql=f"INSERT INTO `adatok`(`név`, `kor`, `magasság`) VALUES ('{nev}', '{kor}', '{magassag}');"
    doItDB(sql)

def update(tablename, mit, mire, felt=0):
    sql=f"UPDATE {tablename} SET {mit}={mire} WHERE {felt};"
    doItDB(sql)

def deleteRows(tablename, felt=0):
    sql=f"DELETE FROM {tablename} WHERE {felt};"
    doItDB(sql)

def truncateTable(tablename):
    sql=f"TRUNCATE TABLE {tablename};"
    doItDB(sql)
    
def dropTable(tablename):
    sql = f"DROP TABLE {tablename};"
    doItDB(sql)

def createTable():
    sql=f"CREATE TABLE adatok ("
    sql+="`id` INT NOT NULL AUTO_INCREMENT ,"
    sql+="`Név` VARCHAR(50) NOT NULL ,"
    sql+="`Kor` INT NOT NULL ,"
    sql+="`Magasság` INT NOT NULL ,"
    sql+="PRIMARY KEY (`id`)"
    sql+=");"
    doItDB(sql)


#createTable()

#update(defaults["DB_TABLE"], "magasság", 140, "kor=9")
#deleteRows(defaults["DB_TABLE"], "kor<18")
#truncateTable(defaults["DB_TABLE"])
#dropTable(defaults["DB_TABLE"])



#rows=selectDB(defaults["DB_TABLE"], "kor, magasság")
#print(rows)

#insertDB("Klaudia", 9, 160)



rows=selectDB(defaults["DB_TABLE"])
for i in rows:
    print(i)
    
    