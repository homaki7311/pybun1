import math
def kumi(a,b):
   jyohen = math.factorial(a)/math.factorial(a-b)
   kahen = math.factorial(b)
   return int(jyohen/kahen)

sousu = input("sousu = ")
sensu = input("erabukazu = ")

n=kumi(int(sousu),int(sensu))
print(n)
