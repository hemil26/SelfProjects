print('\n ***** WELCOME ***** \n')
option=0
def NewMenu():
 print("1.ARE YOU A NEW USER\n")
 print("2.EXISTING USER\n")
 print('3.QUIT\n')
 option=int(input('\n'))
 if(option==1):
   Newuser()
 elif(option==2):
   OldUser()
UserAndPass={}

def Newuser():
  name=str(input('\nName:'))
  age=int(input('Age:'))
  email=str(input('Email id :'))
  if('@' not in email):
    print('\n*** INVALID ***')
    email=str(input('Enter correct email: '))
    while('@' not in email):
      email=str(input('Enter correct email: '))
      if('@' in email):
        break
      else:
        continue
  password=str(input('\nPassword:'))
  repass=str(input('Confirm password:'))
  if(password!=repass):
    print('\n**INCORRECT**')
    repass=str(input('Enter correct password: '))
    while(password!=repass):
      repass=str(input('Enter correct password: '))
      if(password==repass):
        break
      else:
        continue
  user=str(input('\nEnter your username:'))
  if user in UserAndPass:
    print('User name already exists')
    user=str(input('\nEnter your username:'))
    while(user in UserAndPass):
      user=str(input('\nEnter your username:'))
      if(user not in UserAndPass):
        break
      else:
        continue
  UserAndPass[user]=repass
  print('\n*** YOUR ACCOUNT HAS BEEN CREATED ***\n')

def OldUser():
  USER=str(input('Enter your username:'))
  if(USER not in UserAndPass.keys()):
    print('*** INVALID USERNAME ***')
    USER=str(input('Enter your username:'))
    while(USER not in UserAndPass.keys()):
      USER=str(input('Enter correct username: '))
      if(USER in UserAndPass.keys()):
        break
      else:
        continue
  PASS=str(input('Enter your passowrd:'))
  if(UserAndPass.get(USER)!= PASS):
    print('\n*** YOUR PASSWORD DOES NOT MATCH THE USERNAME ***\n')
    PASS=str('Enter correct password:')
    while(UserAndPass.get(USER)!= PASS):
      PASS=str(input('Enter correct password: '))
      if(UserAndPass.get(USER)==PASS):
        break
      else:
        continue
    print('\n ## LOGIN SUCCESFUL ## \n')
  else:
    print('\n ## LOGIN SUCCESSFUL ## \n')

while(option!=3):
  NewMenu()





