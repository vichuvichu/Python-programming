num=int(input("enter a number:"))
n=1
for i in range(0,num):
  for j in range(0,num-2):
    print(end=" ")
  for j in range(0,i+1):
    print(n,end=" ")
    n=n+1
  print()

