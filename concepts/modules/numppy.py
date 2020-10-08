#replace odd no with -1
import numpy as np
arr = np.arange(0,10)
print(arr)
arr[arr%2==1] = -1
print(arr)


## Get common itesm in two numpy array
a = np.array([1,3,5,4,2,3,8])
b = np.array([4,6,3,2,1,7,9,0,11])
print(np.intersect1d(a,b))


