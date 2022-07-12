import telebot
import os
import pandas as pd

TOKEN = '2136516264:AAFR0aaWCNxDIXHA4ybHLGN5nnLxdeuU2q0'

tb = telebot.TeleBot(TOKEN)
# tb.send_message(chatid, message)
# tb.send_message(1090865239, 'gogo power ranger')

import requests
import time

base_url = "https://api.telegram.org/bot2136516264:AAFR0aaWCNxDIXHA4ybHLGN5nnLxdeuU2q0/sendDocument"

my_file = open("stocksToTrade.csv", "rb")

parameters = {
    "chat_id" : "1090865239",
    "caption" : "Here is a list for intraday stocks for you. Copy and Paste them in TradingView."
}


files = {
    "document" : my_file
}

resp = requests.get(base_url, data = parameters, files=files)
# print(resp.text)
my_file = pd.read_csv("stocksToTrade.csv")
df= pd.DataFrame(my_file)
# print(df['0'])
list = []
for stock in df['0']:
    list.append(stock)

# print(list)
s= ""
for item in list:
    s+=item+" "

tb.send_message(1090865239,s)    

