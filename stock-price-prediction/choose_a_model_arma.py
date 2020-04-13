#!/usr/bin/python3

import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.arima_model import ARMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def choose_model(data, lags):
    plot_acf(data.values, lags=lags)
    plt.show()
    ma_order = int(input("Enter the order for MA: "))

    plot_pacf(data.values, lags=lags)
    plt.show()
    ar_order = int(input("Enter the order for AR: "))

    return ar_order, ma_order

def predict(data, date, ar_order, ma_order):
    ar_obj = ARMA(data.values, order=(ar_order, ma_order))
    result = ar_obj.fit(disp=0)

    result.plot_predict(start=0, end=date)
    plt.show()

    return

if __name__ == '__main__':
    fname = input("Enter the filename: ")
    lags = int(input("Enter the lags for correlation plots: "))

    data = pd.read_csv(fname, index_col='Date')
    ar, ma = choose_model(data['Adj Close'], lags)
    print("Best Model is ARMA({}, {})".format(ar, ma))
    predict(data['Adj Close'], 260, ar, ma)