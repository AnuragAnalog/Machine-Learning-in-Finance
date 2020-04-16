#!/usr/bin/python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def rmse(actual, predict):
    error = 0
    for i in range(len(actual)):
        error += (actual[i] - predict[i])**2

    error = error/len(actual)
    error = np.sqrt(error)

    return error

def predict_last_value(prices):
    pred = np.empty_like(prices)
    pred[:1] = prices[:1].values

    for i in range(1, len(pred)):
        pred[i] = np.mean(prices[i-1])

    df = pd.DataFrame(index=prices.index, data=pred, columns=['Predicted Price'])

    return df

def plotting_prices(actual, predict, period):
    plt.title("Prediction using Last Value")
    plt.xlabel("Time Period")
    plt.ylabel("Share Price")

    plt.grid(True)
    plt.plot(period, actual, label="Actual")
    plt.plot(period, predict, label="Predicted Last Value")
    plt.legend()

    plt.show()

if __name__ == '__main__':
    fname = input("Enter the filename: ")

    stock_data = pd.read_csv(fname)

    prices = stock_data['Adj Close']
    predict = predict_last_value(prices)

    plotting_prices(prices, predict, stock_data['Date'])
    print("RMSE is: ", rmse(prices.values, predict.values))