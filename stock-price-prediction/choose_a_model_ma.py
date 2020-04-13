#!/usr/bin/python3

import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.arima_model import ARMA

def choose_model(data, order):
    bic = list()

    for i in range(1, order+1):
        ar_obj = ARMA(data.values, order=(0, i))
        result = ar_obj.fit(disp=0)
        bic.append(result.bic)

    plt.plot(range(1, order+1), bic)
    plt.show()

    min_order = bic.index(min(bic)) + 1

    return min_order

def predict(data, date, order):
    ar_obj = ARMA(data.values, order=(0, order))
    result = ar_obj.fit(disp=0)

    result.plot_predict(start=0, end=date)
    plt.show()

    return

if __name__ == '__main__':
    fname = input("Enter the filename: ")

    data = pd.read_csv(fname, index_col='Date')
    best = choose_model(data['Adj Close'], 5)
    print("Best Model is of order:", best)
    predict(data['Adj Close'], 260, best)