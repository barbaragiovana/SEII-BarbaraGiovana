import numpy as np

a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
print(a)

print(a.sum(axis=None)) 
print(a.sum())
print(a.sum(axis=0)) 
print(a.sum(axis=1)) 

print(a.mean(axis=None)) 
print(a.mean())
print(a.mean(axis=0))
print(a.mean(axis=1)) 

print(a.std(axis=None)) 
print(a.std())
print(a.std(axis=0))
print(a.std(axis=1)) 

print(a.var(axis=None)) 
print(a.var())
print(a.var(axis=0))
print(a.var(axis=1)) 

print(a.min(axis=None)) 
print(a.min())
print(a.min(axis=0))
print(a.min(axis=1)) 

print(a.max(axis=None)) 
print(a.max())
print(a.max(axis=0))
print(a.max(axis=1)) 