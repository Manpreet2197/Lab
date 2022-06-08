import pip._vendor.requests
from pip._vendor import requests

countryCity = 'Brampton'
api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(countryCity = 'Brampton'
)
response = requests.get(api_url, headers={'X-Api-Key': '85PFMA5rymDhOSCMI6zKnw==wNtRNdqXJh5UQbNG'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)