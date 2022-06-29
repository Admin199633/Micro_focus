  
import requests
try:
    res = requests.get('http://127.0.0.1:5000/stop_server')
    if res.ok:
        print(res.json())
except:
    print("Stop-server 5000 Fail")

