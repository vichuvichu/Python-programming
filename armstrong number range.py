for i in range(1000000001):
  n=i
  result=0
  num=len(str(i))
  while(i!=0):
    digit=i%10
    result=result+digit**num
    i=i//10
  if n==result:
    print(n)
