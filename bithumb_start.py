import requests

url = "https://api.bithumb.com/v1/market/all?isDetails=true"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)


url = "https://api.bithumb.com/v1/candles/months?count=1"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)