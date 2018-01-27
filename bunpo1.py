import numpy as np
a = np.array  ([1,2,3,4,5])
b = np.array  ([2,3,4,5,6])

c = b
c[0]=3
# change for c affected b
d = b.copy()
d[0]=1
# change for d not affected b

print (b)
print (np.dot(a,b))
print (d)
print (np.dot(a,d))

print ("sa =",np.dot(a,b)-np.dot(a,d))

