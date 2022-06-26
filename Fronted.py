from selenium import webdriver
import pymysql
driver = webdriver.Chrome(executable_path="https://github.com/photop33/Micro-Focus/blob/main/chromedriver.exe")
driver.get("http://localhost:5000/user/1")
x=driver.find_element_by_xpath('/html/body/pre').text
print(x)


from Backend_testing import user_name
conn = pymysql.connect(host='remotemysql.com', port=3306, user='xiDsE9WxzQ', passwd='FL1Sk29yLg', db='xiDsE9WxzQ')
cursor = conn.cursor()
cursor.execute("SELECT name FROM xiDsE9WxzQ.users;")
for row in cursor:
    if user_name == row[0]:
        print('An ',row[0],' exists in the system')
