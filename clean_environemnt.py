  
import requests
try:
    res = requests.get('http://127.0.0.1:5000/stop_server')
    if res.ok:
        print(res.json())
except:
    print("Stop-server 5000 Fail")


try:
    pic = requests.get('http://127.0.0.1:5001/stop_server')
    if pic.ok:
        print(pic.json())

except:
    print("Stop-server 5001 Fail")

