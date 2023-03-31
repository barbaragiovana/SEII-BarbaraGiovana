import numpy as np

x = np.array([1.0,2.0])
print(x)
print(x.dtype)

x = np.array([1.0,2.0], dtype=np.int64)
print(x)
print(x.dtype)

x = np.array([1.0,2.0], dtype=np.int32)
print(x)
print(x.dtype)

x = np.array([1.0,2.0], dtype=np.float16)
print(x)
print(x.dtype)

x = np.array([1.0,2.0], dtype=np.float32)
print(x)
print(x.dtype)