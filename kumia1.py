import math
def kumi(a,b):
   jyohen = math.factorial(a)/math.factorial(a-b)
   kahen = math.factorial(b)
   return int(jyohen/kahen)

n=kumi(5,3)
print(n)
