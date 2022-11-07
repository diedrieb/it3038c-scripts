import json
import requests

r = requests.get('https://localhost:3000/')
data=r.json()
print(data['name'] + 'is' ['color'])
