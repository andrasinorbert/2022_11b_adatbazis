# Adatbáziselérés Pythonnal

## phpMyAdmin

1. Adatbázis létrehozás
1. Tábla létrehozás
1. User létrehozás

## Python

1. Szükséges adatok elmentése: config.py

    ```py
    defaults= {
        "DB_HOST": "127.0.0.1",
        "DB_PORT": 3306,
        "DB_NAME": "10b",
        "DB_TABLE": "elso",
        "DB_UNAME": "10b_user",
        "DB_PASSWD": "10b_user"
    }
    ```

1. pymysql telepítése

    ```bash
    pip install pymysql
    ```

1. python kód:

    ```py
    import pymysql
    import config
    ```

1. connect db

    ```py
    conn=pymysql.connect(    host=_host,
                        port=_port,
                        user=_user,
                        password=_passwd,
                        database=_dbname)
    ```

1. Cursor létrehozás

    cursor: egy pointer az adatokra

    ```py
    cursor = conn.cursor()
    ```

1. SQL kód megírása: `sql` változó

    ```py
    sql = f"SELECT {oszlopnevekstr} FROM `{tablename}` WHERE {feltetel};"
    ```

1. SQL parancs futtatása

    ```py
    cursor.execute(sql)
    ```

1. Válasz elmentése változóba

    fetch= elhozni, elragadni

    ```py
    rows = cursor.fetchall()
    ```

1. Kapcsolat lezárása

    ```py
    conn.close()
    ```

### Insert Into eltérések

```py
sql = f"INSERT INTO {táblanév}({oszlopnevek}) VALUES ({értékek});"
cursor.execute(sql)
conn.commit() # változások elmentése az adatbázisban
conn.close()
```

