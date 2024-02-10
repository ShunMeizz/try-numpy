import numpy as np

a = np.array([[1,2,3],
             [4,5,6],
             [7,8,"9"]]) #the string 9 makes the whole array as string
print(a)
print(a.dtype)
print(type(a[2][2]))

b = np.array([[1,2,3],
             [4,5,6],
             [7,8,"9"]], dtype=np.int32) #typecast the whole array to int32
print(b)
print(b.dtype)
print((type(b[2][2])))
print(b[2][2].dtype) #the string 9 is now a number



