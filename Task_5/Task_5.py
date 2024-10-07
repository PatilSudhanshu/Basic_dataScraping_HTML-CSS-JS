import requests as rq

cUrl = 'https://api.coinbase.com/v2/exchange-rates'

cheader =  {
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

stockdata = [
    {
    'stockName': 'infy',
     'price': 1964.50,
     'currency': 'INR'
     },
      {
    'stockName': 'TCS',
     'price': 4521.05,
     'currency': 'INR'
     },
      {
    'stockName': 'Google',
     'price': 163.38,
     'currency': 'USD'
     },
     {
    'stockName': 'Amazon',
     'price': 178.50,
     'currency': 'USD'
     }
]

def getCurrencyRates(price,currency):

    queryParams = {
        'currency' : currency
        }



    cResp = rq.get(url = cUrl, headers = cheader, params= queryParams)

    print(cResp.status_code)
    if currency == 'INR':
        USDRate = float(cResp.json()['data']['rates']['USD'])
        print(f'newRate = {USDRate * price}')
        return USDRate * price
    else:
        INRRate = float(cResp.json()['data']['rates']['INR'])
        print(f'newRate = {INRRate * price}')
        return INRRate * price

newStockList = []
for stock in stockdata:
    print(stock['currency'])
    newCurrencyRate = getCurrencyRates(stock['price'],stock['currency'])
    stock['exchangeRate'] = newCurrencyRate
    newStockList.append(stock)

print()
print(newStockList)
print()