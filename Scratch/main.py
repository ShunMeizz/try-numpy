import numpy as np

'''
a = np.array([[1,2,3],
             [4,5,6],
             [7,8,"9"]])  # the string 9 makes the whole array as string
print(a)
print(a.dtype)
print(type(a[2][2]), "\n")

b = np.array([[1,2,3],
             [4,5,6],
             [7,8,"9"]], dtype=np.int32)  # typecast the whole array to int32
print(b)
print(b.dtype)
print((type(b[2][2])))
print(b[2][2].dtype, "\n")  # the string 9 is now a number

# is an object
d = {'1': 'A'}

# will make everything as object
z = np.array([[1,2,3],
            [4,d,6],
            [5,6,"hello"]])
print(z)
print(z.dtype)
print(type(z[2][2]))
print(type(z[1][0])) # it goes back to python default dtype which is 'int' not int32
#print(z[1][0].dtype) AttributeError: 'int' object has no attribute 'dtype'

#Filling Arrays
e = np.full((2,3,4),9)
f = np.zeros((2,3,4))
g = np.ones((2,3,4))
h = np.empty((1,2,3))

for arr in [e,f,g,h]:
    print(arr,"\n")

x_values = np.arange(0,60,5) #provides the stepsize
print(x_values)
y_values = np.linspace(0,60,5) #how many values we want to have
print(y_values)

c1 = np.array([1,2,3])
c2 = np.array([[4],
               [5]])
print(c1+c2)
c1 = np.append(c1, c2)
c1 = np.insert(c1, 5,[6,7,8,9,10])
c1 = np.insert(c1, 0,[-2,-1,0])
print(c1)

i1 = np.array([10,20,30,40,50])
print(np.sqrt(i1))
print(np.sin(i1))
print(np.exp(i1))
print(np.log(i1))

j = np.array([[1,2,3],
              [4,5,6]])

# print(np.delete(j,1))
# print(np.delete(j,1,0)) #axis = 0 means row
# print(np.delete(j,0,1)) #axis = 1 means col

print(j.reshape((3,2)))

var1 = j.flatten()
var1[2] = 100
print(var1)
print(j)

var2 = j.ravel()
var2[2] = 100
print(var2)
print(j)

m1 = np.array([[1,2,3,4,5],
             [6,7,8,9,10]])
m2 = np.array([[11,12,13,14,15],
              [16,17,18,19,20]])

a = np.concatenate((m1,m2), axis=0)
print(a.shape)
print(a,"\n")
b = np.concatenate((m1,m2), axis=1)
print(b.shape)
print(b,"\n")
c = np.stack((m1,m2))
print(c.shape)
print(c,"\n")
d = np.hstack((m1,m2))
print(d.shape)
print(d,"\n")
e = np.vstack((m1,m2))
print(e.shape)
print(e,"\n")

number = np.random.randint(100) #until 100
print(number)
random_arr = np.random.randint(100,size=(2,3,4))
print(random_arr)

np.save("myarray.npy", m1)
np.savetxt("myarray2.csv", m2, delimiter=",")
'''
a = np.load("myarray.npy")
b = np.loadtxt("myarray2.csv", delimiter=",")
print(a)
print(b)









