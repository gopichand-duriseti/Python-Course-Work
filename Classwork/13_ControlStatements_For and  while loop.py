name='gopi'
for ch in name:
    print('ch',' = ',ch)
l=['sanjay','revanth','gopi','gopal']
for name in l:
    print('name','=',name)
d={1:'hello',2:'hii',3:'hey'}
for i,j in d.items():
    print(i,j.capitalize(),sep=' is ')
for i in d.keys():
    print(d[i].capitalize())
for i in d.keys():
    print(f'{i}:{i**2}') #or print(f'{i}:{i*i}')
'''-----------------------------------------------------------------'''
for i in range(1,11):
    print(f'2*{i}={2*i}')
'''-----------------------------------------------------------------'''
email,pwd='xyz@gmail.com','xyz@123'
max_attempt=5
cur_attempt=1
while max_attempt>=cur_attempt:
    e=input("Enter the email: ")
    p=input("Enter the pwd: ")
    if e==email and p==pwd:
        print("Login Successful")
        break
    else:
        max_attempt-=1
        if max_attempt>0:
            print(f"Invalid Login,Attempts Remaining:{max_attempt}")
else:
    print("You have no Attempts left")
    
'''OR'''

email,pwd='xyz@gmail.com','xyz@123'
max_attempt=5
cur_attempt=1
while cur_attempt<=max_attempt:
    e=input("Enter the email: ")
    p=input("Enter the pwd: ")
    if e==email and p==pwd:
        print("Login Successful")
        break
    else:
        print("Invalid email or pwd.Try again!!")
    cur_attempt+=1
else:
    print("Max attempts are done.Try after 5 minutes")  
'''-----------------------------------------------------------------'''

    
