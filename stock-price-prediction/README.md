# Stock Price Prediction

## Installation

Some of the python scripts requires third party libraries like numpy, pandas etc.,
To install them with the required version, run the below command
```shell
sudo pip3 install -r requirements.txt
```
additional to this, it also requires to install one more library talib, which can be one in four steps

### Installing TA-Lib module
* Step 1
Download the tar file
```shell
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
```
```shell
tar -xzf ta-lib-0.4.0-src.tar.gz
```
```shell
cd ta-lib/
```

* Step 2
Install the package
```shell
sudo ./configure
```
```shell
sudo make
```
```shell
sudo make install
```

* Step 3
Install the TA-Lib python wrapper
```shell
sudo pip3 install talib
```

* Step 4
Add path to .bashrc
```shell
echo "export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH" >> ~/.bashrc
```
```shell
source .bashrc
```

## Models
when deciding which model is best, acf plot gives information about MA part, and pacf(partial autocorrelation function) gives info about AR part.

If there is a Positive autocorrelation at lag 1 then we use the AR model
If there is a Negative autocorrelation at lag 1 then we use the MA model

### AR Models

For selecting a good ar model look at the pacf graph first and, include only those lags which are
statistically significant.

### MA Models

ma(t) = average(mu) + some percent of error from the previous predicted value(epsilon(t))

AR and MA models are mostly used on stationary series that is, series which is time invariant, series which has constant mean, constant variance and autocorrelation of lag k in only a function of k.

Thats where ARIMA models come,

### ARIMA Models

this mainly depends on three parameters p, d, q
p is the lag of the autocorrelation, p helps adjust the line that is being fitted to forecast the series
d is the difference which is used to eliminate trend or seasonality and make it a stationary series
q is the lag of the error component, where error is in the time series which is not explained by the trend or seasonality.