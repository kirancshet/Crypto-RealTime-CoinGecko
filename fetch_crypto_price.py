#-------------------------------------------------------------------------------
# Name      :   fetch_crypto_price.py
# Purpose   :   This Python script takes crypto tokens and 
#               fetch real-time market data via CoinGecko 
#               in Python
# Author    :   Kiran Chandrashekhar
# Webste    :   https://sapnaedu.com
# Created   :   26-Dec-2022
#-------------------------------------------------------------------------------

import conf as settings
import requests
import json

#---------------------------------------------------------
#  Fetch Current market price of Crypto from CoinGecko
#  You can get the CoinMarket API Key from your developer account:
#  https://pro.CoinGecko.com/account
#  Refer to the API documentation here: https://www.coingecko.com/en/api/documentation
#---------------------------------------------------------

class CryptoPrice:
    def __init__(self, currency='usd'):
        self.currency = currency.lower()
        self.base_url = r'https://pro-api.coingecko.com/api/v3'  #Premium Account API URL
        self.base_url = r'https://api.coingecko.com/api/v3'      #Free Account  
    
    #---------------------------------------------------------
    #   Fetch Current Market Price of a crypto from CoinGecko
    #---------------------------------------------------------
    def get_current_price(self, token):
        url = f"{self.base_url}/simple/price"
    
        header = {}       
        header['Content-type'] = 'application/json'

        data = {}
        data['ids'] = token
        data['vs_currencies'] = self.currency
        #data['x_cg_pro_api_key'] = settings.API_KEY  #applicable for Premium Account

        response = requests.get(url, headers=header, params=data)
        crypto_info = response.json()
        #print(json.dumps(crypto_info, indent=4))

        crypto_price = crypto_info[token][self.currency]
        #print(crypto_price)

        return crypto_price


    #---------------------------------------------------------
    #  Fetch Current market price of Multiple Crypto from CoinGecko
    #---------------------------------------------------------    
    def get_current_price_multiple(self, token_list:list)->dict:

        crypto_price = {}
        url = f"{self.base_url}/simple/price"
    
        header = {}        
        header['Accepts'] = 'application/json'

        data = {}
        data['ids'] = ",".join(token_list)
        data['vs_currencies'] = self.currency #Supports comma seperated multiple currencies
        #data['x_cg_pro_api_key'] = settings.API_KEY  #applicable for Premium Account

        response = requests.get(url, headers=header, params=data)
        crypto_info = response.json()
        #print(json.dumps(crypto_info, indent=4))

        for token in token_list:
            crypto_price[token] = crypto_info[token][self.currency]
        
        #print(crypto_price)

        return crypto_price



def main():
    obj = CryptoPrice('usd')

    token = 'bitcoin'
    price = obj.get_current_price(token)
    print(price)

    token_list = ['bitcoin','ethereum', 'tether', 'usd-coin', 'dogecoin']
    crypto_price = obj.get_current_price_multiple(token_list)

    print(crypto_price)
   
    
if __name__ == '__main__':
    main()
    print("Done")