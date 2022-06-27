import requests
user_id = "1"

try:
    dic = open ('k8s_url.txt','r')
    read = dic.read()
    url = ""+ read +"/user/"+ user_id +""
    print(url)
    
    res = requests.get(url)
    if res.ok:
        print(res.json())
except:
    res = requests.get('http://127.0.0.1:5500/user/' + user_id + '')
    if res.ok:
        print(res.json())

    


