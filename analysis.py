
# data from : https://www.cryptodatadownload.com/data/binance/

import pandas as pd

from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt

import numpy as np




filename = "../Binance_ETHUSDT_minute.csv"


data = pd.read_csv(filename)

day  = 24 * 60
week = day * 7


fs = 1
N = 100000

chart = np.array(data['open'])

Chart = fft(chart[:N])


f, t, Sxx = signal.spectrogram(chart, fs)

#plt.pcolormesh(t, f, Sxx, shading='gouraud')

plt.plot(20*np.log10(Chart[:N]))

plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()


print('ciao')
