# import urllib2
import requests 
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class handle(object):

    def __init__(self):
        print("Auto Coin module loaded....")

    def get(self, coin_name="BTC", cash_name="USD"):
        self.request_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={}&convert={}"
        self.coin_name = coin_name
        self.cash_name = cash_name
        self.parameters = {
            "id": "",
            "symbol": coin_name,
            "convert": cash_name
        }
        self.actual_url = self.request_url.format(self.parameters["symbol"], self.parameters["convert"]) 
        print self.actual_url
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": "your-key"
        }

        r = requests.get(self.actual_url, headers=headers)

        self.result = json.loads(r.text)

        print self.result

    def catch(self):
        if self.result["status"]["error_code"] == 0:
            return self.result["data"][self.coin_name]["quote"][self.cash_name]["price"]
        else:
            return "wrong format"

    
def test():
    query_obj = handle()
    query_obj.get()
    print query_obj.catch()

def query(coin="BTC", cash="USD"):
    query_obj = handle()
    query_obj.get(coin,cash)
    return query_obj.catch()

if __name__ == "__main__":
    test()