import pymysql
import requests
from flask import request



def Create_Table():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='AFKTvDpMGV', passwd='MXSpb3808w', db='AFKTvDpMGV')
    cursor = conn.cursor()
    conn.autocommit(True)
    name_table="user"
    cursor.execute("CREATE TABLE `AFKTvDpMGV`.`"+ name_table +"` (`ID` INT UNSIGNED NOT NULL,`name` VARCHAR(50) NOT NULL,""`time_column`datetime (`ID`))")
    print("Ready table "+ name_table +"")
    cursor.close()
    conn.close()


def GET(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='xiDsE9WxzQ', passwd='FL1Sk29yLg', db='xiDsE9WxzQ')
    cursor = conn.cursor()
    conn.autocommit(True)
    x=cursor.execute("SELECT * FROM xiDsE9WxzQ.users;")
    result = cursor.fetchall()
    for row in result:
        user_id
        show = str(row[0])
        show1=str(user_id)
        if show == show1:
            user_name = row[1]
            return user_name
    cursor.close()
    conn.close()
X=GET(5)
print(X)
users = {}




def POST(user_id) :
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='xiDsE9WxzQ', passwd='FL1Sk29yLg', db='xiDsE9WxzQ')
    request_data = request.json
    print(request_data, '1')
    user_name = request_data.get('user_name')
    print(user_name)
    users[user_id] = user_name
    conn.autocommit(True)
    cursor = conn.cursor()
    print(user_id,user_name)
    cursor.execute("INSERT INTO xiDsE9WxzQ.users (user_id,name) VALUES (%s,%s)", (user_id,user_name))
    cursor.close()
    conn.close()
    print("success insert_user")
    return user_name


# def user(user_id):
#     if request.method == 'POST':
#         try:
#             from db_connector import POST
#             user_name = POST(user_id)
#             return {'user id': user_id, 'user added': user_name, 'status': 'ok'}, 200  # status code
#         except:
#             return {"status": "error", "reason": "idal ready exists"}, 500
#
# user_id='5'
# user(user_id)




users = {}
def update_user(user_id):
    request_data = request.json
    request_data.get('user_name')
    user_name = request_data.get('user_name')
    users[user_id] = user_name
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='xiDsE9WxzQ', passwd='FL1Sk29yLg', db='xiDsE9WxzQ')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("UPDATE xiDsE9WxzQ.users SET name = '" + user_name + "'  WHERE user_id=" + user_id + "")
    cursor.close()
    conn.close()
    return user_name

def DELETE(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='xiDsE9WxzQ', passwd='FL1Sk29yLg', db='xiDsE9WxzQ')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM xiDsE9WxzQ.users;")
    result = cursor.fetchall()
    for row in result:
        show = str(row[0])
        if show == user_id:
            print(row[1])
            user_name = row[1]
    cursor.execute("DELETE FROM xiDsE9WxzQ.users WHERE user_id = " + user_id + "")
    cursor.close()
    conn.close()
    return user_name


