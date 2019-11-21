import math
n=int(input("enter the number:"))
try:
  result=math.factorial(n)
  print(result)
except:
  print("cannot compute the negative numbers")
