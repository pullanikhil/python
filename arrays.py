import numpy as np
zeroDarray = np.array(10)
oneDarray = np.array([10,11])
twoDarray = np.array([[10,11],[12,13]])
threeDarray = np.array([[[4,5],[6,7],[8,9]]])

print(zeroDarray.ndim)
print(oneDarray.ndim)
print(twoDarray.ndim)
print(threeDarray.ndim)
print(zeroDarray.dtype)
print(oneDarray.shape)
print(twoDarray.shape)
print(threeDarray.shape)
