import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return x*x*x

pi = np.pi
T = 4*pi
jisuu = 15
omega = 2*pi/T
a = []
b = []
for num in range(0,jisuu):
    a.append(quad(lambda x,k : f(x)*np.cos(k*omega*x),-T/2,T/2,args = num)[0])
    b.append(quad(lambda x,k : f(x)*np.sin(k*omega*x),-T/2,T/2,args = num)[0])

def f2(x):
    result = a[0]/2*2/T
    for num in range(1,jisuu):
        result = result + 2/T*a[num]*np.cos(num*omega*x)+2/T*b[num]*np.sin(num*omega*x)
    return result

xx = np.linspace(-T/2,T/2,200)
yy = f2(xx)

plt.plot(xx,yy)
plt.plot(xx,f(xx))
plt.show()
