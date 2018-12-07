import oandapyV20 as opy
import pandas as pd
import oandapyV20.endpoints.trades as trades
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails
import oandapyV20.endpoints.orders as orders
import json

ACCESS_TOKEN = 'c36b759ab5a83d58ca91b5ee1bd8aee1-660f3e0b44165ffca1d2cb6bebf2c495'
ACCOUNT_ID = '101-004-9917560-001'

def main():
    client = opy.API(environment='practice', access_token=ACCESS_TOKEN)
    EUR_USD_STOP_LOSS = 1.10
    EUR_USD_TAKE_PROFIT = 1.16

    mktOrder = MarketOrderRequest(
    instrument="EUR_USD",
    units=10000,
    takeProfitOnFill=TakeProfitDetails(price=EUR_USD_TAKE_PROFIT).data,
    stopLossOnFill=StopLossDetails(price=EUR_USD_STOP_LOSS).data)

    r = orders.OrderCreate(ACCOUNT_ID, data=mktOrder.data)
    try:
        rv = client.request(r)
    except oandapyV20.exceptions.V20Error as err:
        print(r.status_code, err)
    else:
        print(json.dumps(rv, indent=2))

                           


def getTrades():
    r = trades.TradesList(ACCOUNT_ID)
    rv = client.request(r)
    print("RESPONSE:\n{}".format(json.dumps(rv, indent=2))) 

if __name__ == '__main__':
    main()