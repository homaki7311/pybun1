import numpy as np
import matplotlib.pyplot as plt
n = 5
x = np.array([1,2,3,4,5])
y = np.array([6,7,7,9,10])
xy = np.dot(x,y)
xx = np.dot(x,x)
sumy = np.sum(y)
sumx = np.sum(x)

a = np.array([[xx,sumx],[sumx,n]])
b = np.array([[xy],[sumy]])
ina = np.linalg.inv(a)
c = np.dot(ina,b)

xa=np.arange(1,n+1,1)
ya=c[0]*xa+c[1]

plt.plot(x,y,'o')
plt.plot(xa,ya)
plt.show()
