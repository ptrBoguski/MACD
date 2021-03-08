import MACD as ptr
import All_In_Alg
import Test_Alg
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = [20, 5]
# todo commandline arguments
period = 1050
initial_cash = 10000
data = pd.read_csv("example.csv")  # wig20

data_in_period = data.tail(period)
stock_values = data_in_period.get("Otwarcie")
date = data_in_period.get("Data")
stock_values = np.flip(stock_values)
stock_norm = []
date_norm = []
# todo move this to MACD.py
for cell in stock_values:
    stock_norm.append(cell)
for cell in date:
    date_norm.append(cell)
MACD = []
i = 0
for cell in stock_norm:
    if i > 25:
        MACD.append(ptr.MACDC(stock_norm, i, period))
    else:
        MACD.append(0)
    i += 1
i = 0
signal = []
for cell in MACD:
    signal.append(ptr.EMAC(MACD, i, 9,period))
    i += 1

MACD = np.flip(MACD)
signal = np.flip(signal)
sell = []
buy = []
for i in range(0, period - 2):
    if (MACD[i + 1] < signal[i + 1]):
        if (MACD[i] > signal[i]):
            # if(signal[i + 1] < signal [ i]): # check if signal descending
            sell.append(i + 1)
    elif (MACD[i + 1] > signal[i + 1]):
        if (MACD[i] < signal[i]):
            # if(signal[i + 1] > signal [i]): # check if signal ascending
            buy.append(i + 1)

n_w = np.array(stock_norm)


Test_Alg.test_alg(MACD,signal,buy,sell,n_w,All_In_Alg.alg_all_in,"ALL IN", initial_cash,period)
