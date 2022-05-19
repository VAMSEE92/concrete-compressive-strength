import requests
import json
url="http://localhost:8111/api"
data=json.dumps({'cement':15,'slag':4,'ash':35,'water':91,'superplastic':8,'age':7})
r=requests.post(url,data)
print(r.json())