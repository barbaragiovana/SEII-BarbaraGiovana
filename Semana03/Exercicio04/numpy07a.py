import numpy as np

a = np.array([[1,2,6], [3,4,8]])
print(a)
print(a.shape)

print(a[0])
print(a[0][0])
print(a[0,0])
print(a[:,0])
print(a[0,:])
print(a.T)

a = np.array([[1,2], [3,4]])
print(np.linalg.inv(a))
print(np.linalg.det(a))
print(np.diag(a))

c = np.diag(a)
print(np.diag(c))