import requests

user_id = "1"
user_name = 'lior'




resp = requests.get('http://localhost:5000/user/'+ user_id +'')
txt = resp.content
print(txt)
