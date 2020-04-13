#!/usr/bin/python3

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def scale(data):
    scaling = MinMaxScaler()

    scaling.fit(data.values)
    scaled_data = scaling.transform(data.values)

    scaled_data = pd.DataFrame(index=data.index, data=scaled_data, columns=data.columns)

    return scaled_data

if __name__ == "__main__":
    fname = input("Enter the filename: ")

    data = pd.read_csv(fname, index_col='Date')
    print(data.head())

    scaled_data = scale(data)
    scaled_data.to_csv(fname.split('.')[0]+"_preprocessed.csv")