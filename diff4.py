import math
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

#function def

def kansuu1(n):
   x = symbols("x")
   f = diff((x**2-1)**n,x,n)
   
   a = np.arange(-1,1,0.01)
   b = []

   for item in a:
       b.append(1/(2**n*math.factorial(n))*f.subs([(x,item)]))
   return a,b

#main

n = 2
result = kansuu1(n)

plt.plot(result[0],result[1],label='$P_{'+str(n)+'}(x)$')

n = 4
result = kansuu1(n)

plt.plot(result[0],result[1],label='$P_{'+str(n)+'}(x)$')

n = 6
result = kansuu1(n)

plt.plot(result[0],result[1],label='$P_{'+str(n)+'}(x)$')
plt.title('legendre polynomials')
plt.xlabel('x')
plt.ylabel('Pn(x)')
plt.legend()
plt.show()
