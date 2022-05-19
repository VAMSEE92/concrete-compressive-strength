import requests
import json
url="http://ec2-65-0-173-133.ap-south-1.compute.amazonaws.com:8080/api"
data=json.dumps({'cement':15,'slag':4,'ash':35,'water':91,'superplastic':8,'age':7})
r=requests.post(url,data)
print(r.json())