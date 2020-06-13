from Option import *
import numpy as np
import matplotlib.pyplot as plt

sigma_upper = 10
x = np.linspace(1, sigma_upper, sigma_upper)

d = 0
r = 0
T = 1
sigma = 0.1
K = 1

moneyness = np.arange(0.7, 1.4, 0.1)

for i in moneyness[::-1]:
  S = i * K
  y = [Option(S, K, r, d, sigma, T).european_call() for sigma in range(1, sigma_upper+1)]
  plt.plot(x,y, label = 'moneyness = ' + str(round(i,2)))
  plt.xlabel('Volatility')
  plt.ylabel('Option Price')
  plt.legend();