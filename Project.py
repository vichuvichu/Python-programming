print("person details")
a=input("enter the name:")
b=int(input("enter a phn no:"))
source=int(input("enter source:"))
des=int(input("enter destination:"))
if source<0 or des<0:
  print("give valid number")
  exit()
elif source==0 or des==0:
  print("source and des not valid")
  exit()
else:
  dis=abs(des-source)
print("1.car \n 2.bus \n 3.cab \n 4.auto")
select=input()
if select=="1.car":
  x=dis*5
  print(x)
elif select=="2.bus":
  x=dis*10
  print(x)
elif select=="3.cab":
  x=dis*15
  print(x)
elif select=="4.auto":
  x=dis*7
  print(x)
else:
  print("invalid")
print(a,'\n',b,'\n',source,'\n',des,'\n',dis,'\n',x)
