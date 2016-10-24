import numpy as np

a = np.array([1, 2, 3, 4])
print type(a)
print a.shape
print a[0], a[1]

a[0] = 5
print a

b = np.array([[1, 2, 3], [4, 5, 6]])
print b.shape
print b[0,0], b[1,0]
