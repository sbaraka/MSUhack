import requests
import json
api_token = 'stockxheartspartahack'
api_url_base = 'https://gateway.stockx.com'
response = requests.get(api_url_base)
print(response.status_code) #doesnt work