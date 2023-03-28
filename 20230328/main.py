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

rows=selectDB(defaults["DB_TABLE"], "kor, magasság")
print(rows)

def insertDB(nev, kor, magassag):
    conn=connectDB(
        _host=defaults["DB_HOST"],
        _port=defaults["DB_PORT"],
        _user=defaults["DB_USER"],
        _password=defaults["DB_PASSWD"],
        _database=defaults["DB_NAME"]
    )
    cursor=conn.cursor()
    sql=f"INSERT INTO `adatok`(`név`, `kor`, `magasság`) VALUES ('{nev}', '{kor}', '{magassag}');"
    cursor.execute(sql)
    conn.commit()
    conn.close()


insertDB("Klaudia", 9, 160)
rows=selectDB(defaults["DB_TABLE"])
print(rows)