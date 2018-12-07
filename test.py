import oandapyV20 as opy
from configparser import ConfigParser
import pandas as pd
import oandapyV20.endpoints.trades as trades
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails
import oandapyV20.endpoints.orders as orders
import json


def main():
    params = config()
    ACCESS_TOKEN = params[0]
    ACCOUNT_ID = params[1]
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



def config(filename='values.config', section='Forex'):
    parser = ConfigParser()
    parser.read(filename)
    configParams = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            configParams[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return configParams                           


def getTrades():
    r = trades.TradesList(ACCOUNT_ID)
    rv = client.request(r)
    print("RESPONSE:\n{}".format(json.dumps(rv, indent=2))) 

if __name__ == '__main__':
    main()