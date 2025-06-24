import requests
import pandas as pd

url = "https://api.bithumb.com/v1/candles/months?count=200&market=KRW-BTC"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # 3. JSON 데이터로 변환
    data = response.json()

    # 4. DataFrame 생성
    df = pd.DataFrame([data])  # data를 리스트로 감싸서 DataFrame 생성

    # 5. DataFrame 출력 또는 사용
    print(df)

#print(response.text)