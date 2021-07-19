import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 50, 0, 1]) # limits for x and y

for i in range(50):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.1)

plt.show()