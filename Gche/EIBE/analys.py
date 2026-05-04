from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

vol = np.array([-4, -3, -2, -1,  0,                           # HCl-Seite (Pufferbereich)
                 1,  2,  3,  4,  5,  6,  7,  8,  9, 10,       # NaOH-Seite (dein Original)
                11, 12, 13, 14, 15, 16, 17, 18], dtype=float)  # NaOH-Seite erweitert

val = np.array([3.16, 3.40, 3.57, 3.71, 3.83,                 # HCl + x=0
                3.92, 4.00, 4.07, 4.15, 4.22, 4.30, 4.37,     # dein Original
                4.44, 4.51, 4.58, 4.66, 4.74, 4.83, 4.94,
                5.05, 5.20, 5.38, 5.65])  

def model(x, pKs, n_HA0, n_A0):
    n_OH = 0.1 * (x / 1000)
    return pKs + np.log10((n_A0 + n_OH) / (n_HA0 - n_OH))

params, cov = curve_fit(model, vol, val, p0=[4.5, 0.003, 0.001])

print("pKs =", params[0])
print("n_HA0 =", params[1])
print("n_A0 =", params[2])

plt.scatter(vol, val, label="Messdaten")
plt.plot(vol, model(vol, *params), label="Fit", color="orange")
plt.legend()
plt.show()

