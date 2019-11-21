s=input("enter a string:")
length=len(s)
for i in range(length):
  for j in range(i+1):
    print(s[j],end=" ")
  print()
