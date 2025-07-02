import requests

url = "https://api.bithumb.com/v1/market/all?isDetails=true"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    coinList = response.json()
    print("Market data retrieved successfully:")

    print(coinList)