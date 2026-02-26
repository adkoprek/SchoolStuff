import numpy as np
import matplotlib.pyplot as plt


m = np.pi
l = np.pi * 2 ** 2
A = np.pi * 10 ** 2
w1 = 60
w2 = 40

x = np.linspace(0, 100, 1000)
v1 = (w1 + w2)/(m + l) * m + (l * w1 - m * w2)/(m + l) * np.exp(-(m + l)/A * x)
v2 = (w1 + w2)/(m + l) * l - (l * w1 - m * w2)/(m + l) * np.exp(-(m + l)/A * x)

plt.plot(x, v1, label='V1')
plt.plot(x, v2, label='V2')
plt.legend()
plt.xlabel('time')
plt.ylabel('volume')
plt.show()
