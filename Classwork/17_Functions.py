allstatues=True
def send(reel_link,insta_id):
    if allstatues:
        print("send")
        print("seen")
        print("Pending")

send('https::djdjjdkdd.com','dineshini_(70-1)')
#--------------------------------------------------------------------------#
stmt=input() 
a=None
b=None
c=None
for i in stmt:
    if not i.isdigit():
        a,b=stmt.split(i)
        op=i
a,b=int(a),int(b)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def pow(a,b):
    return a**b

if op=='+':
    print(add(a,b))
elif op=='-':
    print(sub(a,b))
elif op =="*":
    print(mul(a,b))
elif op=="/":
    print(div(a,b))
elif op=="%":
    print(mod(a,b))
elif op=="**":
    print(pow(a,b))
#--------------------------------------------------------------------------#
data={'balance':20000,'history':[]}
def cur_bal():
    print(f"Balance:{data['balance']}")
def deposit():
    amount=int(input("Enter the amount: "))
    data['balance']+=amount
    data['history'].append(f"Deposited amount:{amount}")
    print(f"Deposited amount:{amount}")
def withdraw():
    amount=int(input("Enter the amount: "))
    if amount<=data['balance']:
        data['balance']-=amount
        data['history'].append(f"Withdraw amount:{amount}")
        print(f"Withdraw amount:{amount}")
    else:
        print("Insufficient Balance")
def history():
    if history:
        for i in data['history']:
            print(i)
    else:
        print('No History')

while True:
    print()
    print('1.Current Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.History')
    print('0.Exit')
    ch=int(input("Enter you choice: "))
    if ch==1:
        cur_bal()
    elif ch==2:
        deposit()
    elif ch==3:
        withdraw()
    elif ch==4:
        history()
    elif ch==0:
        break
    else:
        print("Invalid Choice")