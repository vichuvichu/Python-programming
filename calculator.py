a=int(input("enter num1:"))
b=int(input("enter num2:"))
print("1.addition\n2.sub\n3.mul\n4.div\n5.square\n6.percentage%\n7.exit")
select=input("select the operation:")
if select=="1.addition":
  print(a+b)
elif select=="2.sub":
  print(a-b)
elif select=="3.mul":
  print(a*b)
elif select=="4.div":
  print(a/b)
elif select=="5.square":
  print((a+b)**2) 
elif select=="6.percentage%":
  print((a/b)*100)
elif select=="7.exit":
  print("invalid")
  exit()
