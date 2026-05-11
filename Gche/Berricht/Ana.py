import numpy as np
import matplotlib.pyplot as plt

x = np.array([i for i in range(0, 19)], dtype=float) 

y = np.array([3.83, 3.92, 4.00, 4.07, 4.15, 
              4.22, 4.30, 4.37, 4.44, 4.51, 
              4.58, 4.66, 4.74, 4.83, 4.94, 
              5.05, 5.20, 5.38, 5.65])

window_start = 12
window_end = 18

def gram(vol, pH):
    return vol * (10 ** -pH)

gram_data = gram(x, y)

plt.plot(x, gram_data)

linear_x    = x[(window_start-1):window_end]
linear_data = gram_data[(window_start-1):window_end]
poly = np.polyfit(linear_x, linear_data, 1)

Ks = -poly[0]
offset = poly[1]
print("Offset:", offset)
print("Ka:", Ks)
print("pKa:", -np.log10(Ks))

plt.show()
