import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# [[ 6.0  8.0]
#  [10.0 12.0]]
print x + y

# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print x - y

# [[ 5.0 12.0]
#  [21.0 32.0]]
print x * y

# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print x / y

# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print np.sqrt(x)