import pip._vendor.requests
from pip._vendor import requests

city = 'Brampton'
api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': '85PFMA5rymDhOSCMI6zKnw==wNtRNdqXJh5UQbNG'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)