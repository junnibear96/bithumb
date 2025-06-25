import requests
import pymysql
import time

def dbconnect() : 
    conn = pymysql.connect (host='localhost', port=3306, user ='root',password='Tnnmjni47e$',db='trade_coin',charset='utf8')
    return conn 

def insertFetch(data):
    try:
        conn = dbconnect()
        if(conn):
            cur = conn.cursor()
            sql = """INSERT INTO coin_trade (
                market, trade_date, trade_time, trade_date_kst, trade_time_kst, trade_timestamp,
                opening_price, high_price, low_price, trade_price, prev_closing_price, change_status,
                change_price, change_rate, signed_change_price, signed_change_rate, trade_volume,
                acc_trade_price, acc_trade_price_24h, acc_trade_volume, acc_trade_volume_24h,
                highest_52_week_price, highest_52_week_date, lowest_52_week_price, lowest_52_week_date, timestamp
            ) VALUES (
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s, %s
            );"""

            values = (
                data[0]['market'], data[0]['trade_date'], data[0]['trade_time'], data[0]['trade_date_kst'], data[0]['trade_time_kst'], data[0]['trade_timestamp'],
                data[0]['opening_price'], data[0]['high_price'], data[0]['low_price'], data[0]['trade_price'], data[0]['prev_closing_price'], data[0]['change'],
                data[0]['change_price'], data[0]['change_rate'], data[0]['signed_change_price'], data[0]['signed_change_rate'], data[0]['trade_volume'],
                data[0]['acc_trade_price'], data[0]['acc_trade_price_24h'], data[0]['acc_trade_volume'], data[0]['acc_trade_volume_24h'],
                data[0]['highest_52_week_price'], data[0]['highest_52_week_date'], data[0]['lowest_52_week_price'], data[0]['lowest_52_week_date'], data[0]['timestamp']
            )

            cur.execute(sql, values)
            conn.commit()
            print("complete insert")
    except Exception as e:
        print(e.args)
        if hasattr(e, 'message'):
            print(e.message)
        print("db insert error")
    finally:
        conn.close()


url = "https://api.bithumb.com/v1/market/all?isDetails=true"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    coinList = response.json()
    print("Market data retrieved successfully:")

i = 0
while i < len(coinList):
    coin = coinList[i]
    if(i > 49):
        print(f"Fetching ticker data for market: {coin['market']}")
        time.sleep(60)  # Wait for 60 second before the next request
    url = f"https://api.bithumb.com/v1/ticker?markets={coin['market']}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.text) # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print("Ticker data retrieved successfully:")
        print(data)
        # Example of accessing specific fields
        print(f"Current Price: {str(data[0]['opening_price'])} KRW")
        insertFetch(data)
        # You can also insert the data into your database here
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        print(response.text)
    i += 1