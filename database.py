import pymysql
if __name__ == '__main__':

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='wjxtest')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from job")
    cursor.nextset()
    obj = cursor.fetchall()
    print(obj)
    conn.commit()
    cursor.close()
    conn.close()
