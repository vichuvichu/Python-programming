data={}
data ["accno1"]=123456788
data ["accno2"]=56872378509
data ["accno3"]=43576879808809
print(data)
print("enter the details")
firstname=input("first name:")
lastname=input("last name:")
create_username=input("username:")
create_password=input("password:")
accno4=int(input("accno:"))
print("select the operations,\n,1.withdraw,\n,2.deposit,\n,3.balance_enquiry,\n,4.display_details")
select=(input())
if select=="1.withdraw":
  min_amount=1000
  amount=int(input("enter the amount:"))
  #if amount<1000:
    #again=int(input("enter the amount above 1000:")
#print(firstname+" "+lastname,'\n',create_username,'\n',create_password,)
  #else:
    #print("invalid")
#print("thank you")
#exit()
