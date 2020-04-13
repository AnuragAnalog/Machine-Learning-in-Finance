#!/usr/bin/python3

import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

def acf_plot(data, lags):
    plot_acf(data, lags=lags, alpha=0.05)
    plt.show()

    return

if __name__ == '__main__':
    fname = input("Enter the filename: ")

    data = pd.read_csv(fname, index_col='Date')
    acf_plot(data['Adj Close'], 20)