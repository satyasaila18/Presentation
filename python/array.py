import numpy as np
arr=list(map(int,input("Enter array with spaces separated :").split()))
print(arr)
arr.sort()
print(arr)
arr1=np.array([arr])

mat=arr1.reshape(2,3)
print(mat)

