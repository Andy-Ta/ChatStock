import json
import requests

def getStockPrices(stock):
    r = requests.get("http://conu.astuce.media:9993/api/finance/security/{}_XNGS/quote".format(stock))
    data = r.json()
    data = data[0]
    response = []
    response.append('Open: ' + str(data['open']))
    response.append('High: ' + str(data['high']))
    response.append('Low: ' + str(data['low']))
    response.append('Close: ' + str(data['close']))
    return response

def getTop3Gainers():
    r = requests.get("http://conu.astuce.media:9993/api/finance/group/XNGS_TOP_GAINERS_TREP/securities/quote")
    data = r.json()
    response = []
    for x in range(0, 3):
        response.append(data[x]['security']['ticker_code'] + ": " + str(data[x]['quote']['percent_change']) + '% change')
    return response
    
def getTop3Leaders():
    r = requests.get("http://conu.astuce.media:9993/api/finance/group/XNGS_NASDAQ100_zLEADERS/securities/quote")
    data = r.json()
    response = []
    for x in range(0, 3):
        response.append(data[x]['security']['ticker_code'])
    return response