import numpy as np

a = np.array([[1,2], [3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors)

b = eigenvectors[:,0] * eigenvalues[0]
print(b)
c = a @ eigenvectors[:,0]
print(c)

print(b==c)
print(np.allclose(b,c))