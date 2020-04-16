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

def predict_ma(prices, n):
    pred = np.empty_like(prices)
    pred[:n] = prices[:n].values

    for i in range(n, len(pred)):
        pred[i] = np.mean(prices[i-n:i])

    df = pd.DataFrame(index=prices.index, data=pred, columns=['Predicted Price'])

    return df

def hyperparameter_tuning_plot(prices, linear_space):
    rmse_vals = list()
    for n in linear_space:
        prediction = predict_ma(prices, n)
        value = rmse(prices.values, prediction.values)
        rmse_vals.append(value)

    plt.title("RMSE for various N.")
    plt.xlabel("RMSE")
    plt.ylabel("N")

    plt.grid(True)
    plt.plot(linear_space, rmse_vals)
    plt.show()

def plotting_prices(actual, predict, period):
    plt.title("Prediction using Moving Average")
    plt.xlabel("Time Period")
    plt.ylabel("Share Price")

    plt.grid(True)
    plt.plot(period, actual, label="Actual")
    plt.plot(period, predict, label="Predicted Moving Average")
    plt.legend()

    plt.show()

if __name__ == '__main__':
    fname = input("Enter the filename: ")

    stock_data = pd.read_csv(fname)

    prices = stock_data['Adj Close']
    predict = predict_ma(prices, 2)

    plotting_prices(prices, predict, stock_data['Date'])
    hyperparameter_tuning_plot(prices, range(2, 21))