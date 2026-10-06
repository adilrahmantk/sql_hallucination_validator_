import urllib.request
import json
import time

req = urllib.request.Request(
    'http://localhost:5000/api/v1/generate-and-validate',
    data=json.dumps({"prompt": "Show all customers from USA", "dialect": "sqlite"}).encode(),
    headers={'Content-Type': 'application/json'}
)

print("Sending request...")
start = time.time()
try:
    with urllib.request.urlopen(req) as res:
        print('HTTP', res.status)
        print(res.read().decode())
except urllib.error.HTTPError as e:
    print('HTTP ERROR', e.code)
    print(e.read().decode())
except Exception as e:
    print('EXCEPTION', type(e), e)
print(f"Elapsed: {time.time() - start:.2f}s")
