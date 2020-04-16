#!/usr/bin/python3

import sys
import pandas as pd
import yfinance as yf

def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)

    fname = str(ticker)+"_"+str(start_date)+"_"+str(end_date)+".csv"
    data.to_csv(fname)

    return

if __name__ == '__main__':
    ticker = input('Enter the ticker: ')
    start = input('Enter the start-date(YYYY-MM-DD): ')
    end = input('Enter the end-date(YYYY-MM-DD): ')

    get_data(ticker, start, end)