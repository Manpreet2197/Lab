
import pip._vendor.requests
from pip._vendor import requests
import random

# api_url = 'https://ptsv2.com/t/labwork/post'
# usernumber = random.randint(0,150)
# payload = {"userId": usernumber,
# "username":'labwork',
# 'userpass':'123',
# 'favcolour':'yellow',
# 'favnumber':41,
# }
# headers = {'content-type': 'application/json'}
 
# r = requests.post(api_url, auth=('labwork','123'), data=payload, headers=headers)

get_uri='https://ptsv2.com/t/labwork/d/latest/json'
g = requests.get(get_uri)
print(g.json())

