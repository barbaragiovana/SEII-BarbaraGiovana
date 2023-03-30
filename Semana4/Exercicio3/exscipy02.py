import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d

x = np.linspace(0, 10, 10)
y = x**2 * np.sin(x)
plt.scatter(x,y)
plt.show()

f = interp1d(x, y, kind='cubic')
x_dense = np.linspace(0, 10, 100)
y_dense = f(x_dense)

plt.plot(x_dense, y_dense)
plt.scatter(x, y)
plt.show()