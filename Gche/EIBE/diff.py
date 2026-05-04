import matplotlib.pyplot as plt


x = [i for i in range(-8, 21)]
data = [
    1.88,
    2.03,
    2.33,
    2.78,
    3.16,
    3.40,
    3.57,
    3.71,
    3.83,
    3.92,
    4.00,
    4.07,
    4.15,
    4.22,
    4.30,
    4.37,
    4.44,
    4.51,
    4.58,
    4.66,
    4.74,
    4.83,
    4.94,
    5.05,
    5.20,
    5.38,
    5.65,
    6.31,
    10.56
]

x_diff = []
diffs = []

for i in range(1, len(data)):
    x_diff.append(i - 0.5 - 7)
    diffs.append(data[i] - data[i - 1])

plt.plot(x, data)
plt.plot(x_diff, diffs)
plt.show()

