
import requests as rq

curl = 'https://api.coinbase.com/v2/exchange-rates'

cheader =  {
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

stockdata = [
    {
     'stockName': 'infy', 
     'price': 1964.50, 
     'currency': 'INR', 
     'toChange': 'SGD'
     },
    {
     'stockName': 'TCS', 
     'price': 4521.05, 
     'currency': 'INR', 
     'toChange': 'USD'
     },
    {
    'stockName': 'Google', 
    'price': 163.38, 
    'currency': 'USD', 
    'toChange': 'INR'
    },
    {
    'stockName': 'UNITED-OVERSEAS-BANK', 
    'price': 36.60, 
    'currency': 'SGD', 
    'toChange': 'USD'
    },
    {
    'stockName': 'BPCL', 
    'price': 366.6, 
    'currency': 'INR', 
    'toChange': 'JPY'
    },
    {
    'stockName': 'Reliance', 
    'price': 2723.85, 
    'currency': 'INR', 
    'toChange': 'GBP'
    },
    {
    'stockName': 'Amazon', 
    'price': 132.70, 
    'currency': 'USD', 
    'toChange': 'EUR'
    },
    {
    'stockName': 'Microsoft', 
    'price': 317.42, 
    'currency': 'USD', 
    'toChange': 'JPY'
    },
    {
    'stockName': 'Tesla', 
    'price': 261.75, 
    'currency': 'USD', 
    'toChange': 'INR'
    },
    {
    'stockName': 'DBS-Bank', 
    'price': 34.50, 
    'currency': 'SGD', 
    'toChange': 'GBP'
    },
    {
    'stockName': 'Samsung', 
    'price': 67100, 
    'currency': 'KRW', 
    'toChange': 'INR'
    },
    {
    'stockName': 'Apple', 
    'price': 174.55, 
    'currency': 'USD', 
    'toChange': 'SGD'
    },
    {
    'stockName': 'ICICI', 
    'price': 944.15, 
    'currency': 'INR', 
    'toChange': 'EUR'
    },
    {
    'stockName': 'HDFC', 
    'price': 1501.35, 
    'currency': 'INR', 
    'toChange': 'JPY'
    },
    {
    'stockName': 'Facebook', 
    'price': 302.56, 
    'currency': 'USD', 
    'toChange': 'GBP'
    },
    {
    'stockName': 'Netflix', 
    'price': 391.60, 
    'currency': 'USD', 
    'toChange': 'EUR'
    },
    {
    'stockName': 'BYD', 
    'price': 252.20, 
    'currency': 'HKD', 
    'toChange': 'INR'
    },
    {
    'stockName': 'NVIDIA', 
    'price': 464.40, 
    'currency': 'USD', 
    'toChange': 'JPY'
    },
    {
    'stockName': 'Toyota', 
    'price': 2385.50, 
    'currency': 'JPY', 
    'toChange': 'INR'
    },
    {
    'stockName': 'Axis-Bank', 
    'price': 930.50, 
    'currency': 'INR', 
    'toChange': 'SGD'
    }
]


import requests as rq

# Function to fetch currency exchange rates
def getCurrencyRates(price, from_currency, to_currency):
    # Query parameters for the API
    queryParams = {'currency': from_currency}

    # Fetching response from the API
    cResp = rq.get(url=curl, headers=cheader, params=queryParams)
    
    # Check if the request was successful
    if cResp.status_code == 200:
        # Parse the JSON response
        data = cResp.json()
        
        # Extract the exchange rate for the target currency
        exchange_rate = data['data']['rates'].get(to_currency)
        
        if exchange_rate:
            # Calculate the converted price
            converted_price = price * float(exchange_rate)
            return converted_price, exchange_rate
        else:
            print(f"Exchange rate for {to_currency} not found.")
            return None, None
    else:
        print(f"Failed to get currency rates. Status Code: {cResp.status_code}")
        return None, None

# Loop through stock data and convert prices
for stock in stockdata:
    stock_name = stock['stockName']
    price = stock['price']
    from_currency = stock['currency']
    to_currency = stock['toChange']
    
    converted_price, exchange_rate = getCurrencyRates(price, from_currency, to_currency)
    
    if converted_price:
        print(f"{stock_name}: {price} {from_currency} = {converted_price} {to_currency} (Exchange Rate: {exchange_rate})")
