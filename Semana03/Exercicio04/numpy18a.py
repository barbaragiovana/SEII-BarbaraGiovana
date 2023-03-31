import numpy as np


data = np.loadtxt('spanbase.csv', delimiter=",",dtype=np.float32)
print(data.shape, data.dtype)

data = np.genfromtxt('spanbase.csv', delimiter=",", dtype=np.float32)
print(data.shape)