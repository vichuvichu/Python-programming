n=int(input("enter how many terms to print the fibonacci series you want:"))
first=0
second=1
for i in range(n):
  print(first)
  result=first
  first=second
  second=result+second
