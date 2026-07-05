import json
import urllib.request
import urllib.error

url = 'http://127.0.0.1:8000/api/token/'
data = json.dumps({'username': 'Admin', 'password': 'Admin#12345'}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
try:
    res = urllib.request.urlopen(req, timeout=10)
    print('STATUS', res.status)
    print(res.read().decode())
except urllib.error.HTTPError as e:
    print('HTTP', e.code)
    print(e.read().decode())
except Exception as exc:
    print('ERR', exc)
