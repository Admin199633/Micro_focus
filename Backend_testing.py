import requests

user_id = "1"
user_name = 'lior'

resp = requests.post('http://127.0.0.1:5000/user/' + user_id + '', json={"user_name": "" + user_name + ""})
print(resp)
txt = resp.ok
print(txt)


resp = requests.get('http://localhost:5000/user/'+ user_id +'')
txt = resp.content
print(txt)


# #
# res = requests.put('http://127.0.0.1:5000/user/' + user_id + '')
# if res.ok:
#     print(res.json())
#
# resp = requests.delete('http://localhost:5000/user/'+ user_id +'')
# txt = resp.ok
# print(txt)
