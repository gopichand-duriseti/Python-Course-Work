'''
bullets=10
while bullets>0:
    if bullets==5:
        print('Dead')
        break
    print(f'Bullets are left-You can shoot()')
    bullets-=1
else:
    print("Game over")

#PRIME NUMBERS
fact=0
n=int(input('Enter n:'))
for i in range(2,(n//2)+1):
    if n%i==0:
        fact+=1
if fact==0:
    print(f'{n} is prime number\nFactors count={fact}')
else:
    print(f'{n} is not prime number\nFactors count={fact}')
'''
#assertion is only useful for the developers #Don't use much
'''amt=int(input("Enter amount: "))
#if you give -56 there is no restriction to print but it is an error
assert amt>0,"Amount needs to be positive"
print(amt)

data={"BuyNow":True,"Bank":True,"Login":True}
assert data['BuyNow'],data['Bank']
print("Proceed order")'''


#Check balance,withdraw,deposit,view transactions
d={}
cred={'gopi':{'pin':1234,'cur_bal':10000,'history':[]},'hari':{'pin':1234,'cur_bal':20000,'history':[]},'arjun':{'pin':1234,'cur_bal':30000},'history':[]}
acname=input("Enter acnt holder name: ")
balance=cred[acname]['cur_bal']
pin=int(input("Enter pin no: "))
if cred[acname]['pin']==pin:  
        print('Login Successful')
        print("Welcome To ATM")
        s=[]
        while True:
              print()
              print("1.Check Balance")
              print("2.Withdraw amount")
              print("3.Deposit amount")
              print("4.View Transactions")
              ch=int(input("Enter choice: "))
              print()
              if ch==0:
                  break
              elif ch==1:
                  print(f'Balance remaining is ₹{balance}')
                  cred[acname]['cur_bal']=balance
              elif ch==2:
                  Withdraw_amount=int(input("Enter Withdrawal Amount: "))
                  if Withdraw_amount<=balance:
                        balance-=Withdraw_amount
                        print(Withdraw_amount)
                        s.append(f'Withdrawal Amount:{Withdraw_amount}')
                  else:
                      print("Insufficient Balance")
              elif ch==3:
                  Deposit_amount=int(input("Enter Deposit Amount: "))
                  balance+=Deposit_amount
                  print(Deposit_amount)
                  s.append(f'Deposit Amount:{Deposit_amount}')
              elif ch==4:
                  for i in s:
                    cred[acname]['history'].append(i)
                    print(i)
              else:
                  print('Invalid Choice')

else:
    print('Invalid login')

print(cred)