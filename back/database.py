import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='workshop',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def select(sql):
    # if "SELECT" not in sql or "select" not in sql:
    #     return "Not select request"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return result
    finally:
        # connection.close()
        pass

def insert(sql):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()
        return "Commit OK"
    finally:
        # connection.close()
        pass
