import requests

url = "https://api.bithumb.com/v1/orderbook?markets=KRW-BTC"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
if response.status_code == 200:
    data = response.json()
    print("Orderbook data retrieved successfully:")
    print(data)