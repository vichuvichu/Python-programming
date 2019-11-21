num=int(input("enter the rows:"))
for i in range(0,num):
  for j in range(0,num-i-1):
    print(end=" ")
  for j in range(i+1):
    print("*",end=" ")  
  print()
for i in range(num-1,0,-1):
  for j in range (0,num-1-i+1):
    print(end=" ")
  for j in range(0,i):
   print("*",end=" ")
  print()
