import random
data={}
def create():
  data['acc_no']=random.randint(1000000000,9999999999)
  data['bal']=10000
  print('\nYour account number is:',data['acc_no'])
  #getting users name----------------------------------
  namerun=True
  while namerun:
    namerun=False
    data['name']=input('Type your name: ')
    if data['name'].strip()=='':
      print('name')
      namerun=True
      continue
    for i in data['name'].lower():
      if not 97<=ord(i)<=122:
        print('\nAs far as I know name contains only alphabets, not numbers or anyother!\nnow try again\n')
        namerun=True
        break
      
      
  #user name obtained-------------------------------
  phrun=True
  while phrun:
    phrun=False
    try:
      data['ph']=int(input('Type your phone number: '))
    except ValueError:
      print('\nA phone number contains number not anything else\nTry again\n')
      phrun=True
      continue
    if len(str(data['ph']))!=10:
      print('\nMy god! phone numbers have 10 numbers like 7550309683 not {} this is not even a phone number!\nTry again\n'.format(data['ph']))
      phrun=True
      continue
  #phone number vaagiyatchu----------------------------
  passrun=True
  while passrun:
    passrun=False
    data['ps']=input('\nA Password must contain atleast 8 characters, so keep that in mind and \ntype one: ')
    if len(data['ps'])<8:
      print('\nWhat did I just told you??\nTry again\n')
      passrun=True
      continue
  #password done------------------------------------
  return data

def login():
  namerun=True
  while namerun:
    namerun=False
    name=input('Type your name: ')
    if name!=data['name']:
      namerun=True
      print('\nNo such username\n')
      continue
  psrun=True
  while psrun:
    psrun=False
    ps=input('Type your password: ')
    if ps!=data['ps']:
      print('Wrong!')
      psrun=True
      continue
  acrun=True
  while acrun:
    acrun=False
    acno=input('Type your account number: ')
    if int(acno)!=data['acc_no']:
      print('\nWrong!\nTry again\n')
      acrun=True
      continue
  print('Success')
#getting user choice--------------------------------------------

chrun=True
i=0
first=True
while chrun:
  chrun=False
  try:
    ch=int(input("1.Create new account\n2.Login to existing account\nEnter your choice: "))

  except ValueError:
    print('\nType an integer not characters or symbols\nTry again\n')
    chrun=True
    continue

  if ch==1:
    create()
    first=False
    chrun=True
    continue
  elif ch==2:
    if first:
      i+=1
      print('\ninu yedhu create yae panala, Yaara yematha paakura?\nCreate new kudu{}\n'.format(i) if i==1 else '\nAdey yevalovaati soldradhu!\ninnu yedhu create panala {} time soldraen\n'.format(i))
      chrun=True
      continue
    login()
  else:
    print('\nInvalid choice choices are between(1-2)\n')
    chrun=True
    continue
#user choice done-----------------------------------------------





'''
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
'''
