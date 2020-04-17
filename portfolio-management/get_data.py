#!/usr/bin/python3

import numpy as np
import pandas as pd
import yfinance as yf

def store_data(tickers):
    cols = []
    collection = pd.DataFrame()

    for tick in tickers:
        stock_name = tick.split('.')[0]
        cols.append(stock_name)
        data = yf.download(tickers=tick, start='2015-01-01', end='2020-04-13', progress=True)
        collection[stock_name] = data['Adj Close']
        print("Fetched {} prices".format(stock_name))

    collection.index = data.index
    collection.columns = cols

    return collection

if __name__ == '__main__':
    stocks = ['SBIN.NS', 'HDFCBANK.NS', 'CANBK.NS', 'YESBANK.NS', 'BANKBARODA.NS', 'ICICIBANK.NS']
    shares = store_data(stocks)
    shares.to_csv('data.csv')