import numpy as np

a = np.arange(1,7)
print(a)
print(a.shape)

b = a.reshape((2,3))
print(b)

c = a.reshape((3,2))
print(c)

d = a[np.newaxis,:]
print(d)
print(d.shape)

e = a[:,np.newaxis]
print(e)
print(e.shape)