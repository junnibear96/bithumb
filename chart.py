import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

url = "https://api.bithumb.com/v1/candles/months?count=200&market=KRW-BTC"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # 3. JSON 데이터로 변환
    data = response.json()

    # 4. DataFrame 생성
    df = pd.DataFrame([data])  # data를 리스트로 감싸서 DataFrame 생성
    # Create DataFrame
    df = pd.DataFrame(data)
    df['candle_date_time_kst'] = pd.to_datetime(df['candle_date_time_kst'])
    df = df.sort_values('candle_date_time_kst')
    df['date_num'] = mdates.date2num(df['candle_date_time_kst'])

    # Plot
    plt.figure(figsize=(10,6))

    # High-Low as vertical lines
    for _, row in df.iterrows():
        plt.plot([row['date_num'], row['date_num']], [row['low_price'], row['high_price']], color='gray', linewidth=2)

    # Trade Price as line
    plt.plot(df['date_num'], df['trade_price'], marker='o', color='blue', label='Trade Price (Close)')

    # Format dates
    plt.gca().xaxis_date()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.title('KRW-BTC Price Trend')
    plt.xlabel('Date (KST)')
    plt.ylabel('Price (KRW)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()