import csv

import ccxt
from binance.client import Client

class accessManager:
    userKey_API = ""
    userKey_Secret = ""
    client = Client()
    binance = ccxt.binance()

    def __init__(self):
        print("Access Manager Created!")
        with open("apikeys.txt") as f:
            lines = f.readlines()
            self.userKey_API = lines[0].strip()
            self.userKey_Secret  = lines[1].strip()
            self.client = Client(api_key = self.userKey_API, api_secret = self.userKey_Secret)
            self.binance = ccxt.binance(config={'apiKey' : self.userKey_API, 'secret' : self.userKey_Secret, 'enableRateLimit' : True})

    def getData(self):
        data = self.client.futures_historical_klines(symbol = "XRPUSDT", interval = '1h', start_str = "2020-01-06", end_str = "2023-06-20")
        with open('klinesRaw_XRPUSDT.csv', 'w') as file :
            write = csv.writer(file)
            write.writerows(data)
        
        print("Imported " + str(len(data)) + " days worth of data")
        
    def getBalance(self):
        balance = self.binance.fetch_balance(params={"type" : "spot"})
        print(balance['RSR'])


"""
data = client.futures_historical_klines(
    symbol = "XRPUSDT",
    interval = '1d',
    start_str = "2020-01-06",
    end_str = "2023-06-20"
    )

with open('klinesRaw_XRPUSDT.csv', 'w') as file :
    write = csv.writer(file)
    write.writerows(data)
"""

