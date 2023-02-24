import pymysql

connection = pymysql.connect(host="DB_host",
                port="3306",
                user="sosin",
                password="password",
                database="db_name",
                charset="utf8mb4")

# 한개만 INSERT
with connection.cursor() as cursor:
    sql = "INSERT INTO `table_name` (`column1`, `column2`) \
        VALUES (%s, %s)"

    cursor.execute(sql, ('sosin', 'jason@fins.ai'))

    connection.commit()

# 여러개 INSERT
with connection.cursor() as cursor:
    sql = "INSERT INTO `table_name` (`column1`, `column2`) \
        VALUES (%s, %s)"

    cursor.executemany(sql, [
        ('sosin', 'jason@fins.ai'),
        ('hong', 'test@gmail.com'),
    ])

    connection.commit()