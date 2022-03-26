#원화마켓 - 비트코인, 이더리움, 리플 데이터 가져오기

import requests

url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC%2C%20KRW-ETH%2C%20KRW-XRP"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)
