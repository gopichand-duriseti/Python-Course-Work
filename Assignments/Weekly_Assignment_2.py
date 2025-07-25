#1)AUTOMATED SALARY TAX CALCULATOR
salary=float(input("Enter Salary: "))
tax=0
if salary>100000:
        print(salary*0.3)
elif salary>500000:
    print(salary*0.2)
elif salary>250000:
    print(salary*0.05)
else:
    print("No Tax")
'''------------------------------------------------------------------------'''
#2)MOVIE TICKET PRICING SYSTEM
n=int(input())
tot=0
for _ in range(n):
    a=int(input())
    if a>+60:
        tot+=120
    elif a>=19:
        tot+=150
    elif a>=5:
        tot+=100
print(tot)
'''------------------------------------------------------------------------'''
#3)ELECTRICITY BILL GENERATOR
units=int(input())
bill=0
if units<=100:
    bill+=units*1.5
elif 101<=units<=200:
    bill+=units+(units-100)*2.5
elif 201<=units<=500:
    bill+=units+(units-200)*4
else:
    bill+=1600+(units-500)*6
print(bill)
'''------------------------------------------------------------------------'''
#4)CAR PARKING FEE CALCULATOR
hrs=int(input())
fee=0
if hrs<=2:
    print(30)
elif hrs>2 and hrs<24:
    print(30+(hrs-2)*10)
elif hrs>=24:
    print(200)
'''------------------------------------------------------------------------'''
#5)PRODUCT INVENTORY CHECKER
name=input()
qua=int(input())
if qua==0:
    print('Out of Stock')
elif qua>0 and qua<11:
    print('Low Stock')
elif qua>10 and qua<50:
    print('In Stock')
else:
    print('Over stocked')
'''------------------------------------------------------------------------'''
#6)PATTERN-Row-wise Alternating 0 and 1
n=int(input())
for i in range(n):
    for j in range(n):
        if i%2!=0 and j%2==0:
            print(1,end=" ")
        elif i%2==0 and j%2!=0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
                #OR
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print(0,end=' ')
        else:
            print(1,end=" ")
    print()
'''------------------------------------------------------------------------'''
#7)GYM SUBSCRIPTION BILLING(Menu Driven Program)
while True:
    print('Menu:\n')
    print('0.exit')
    print('1.Monthly-Rs 500')
    print('2.Quarterly-Rs 1300')
    print('3.Yearly-Rs 5000')
    ch=int(input())
    ppl=int(input())
    if ch==0:
        break
    elif ch==1:
        print(ppl*500)
    elif ch==2:
        print(ppl*1300)
    elif ch==3:
        print(ppl*5000)
'''------------------------------------------------------------------------'''
#8)BILLING BOT
amt=float(input("Enter amount: "))
if amt<1000:
    print(amt)
elif amt>999 and amt<5000:
    print(amt-(amt*0.05))
elif amt>5000 and amt<10000:
    print(amt-(amt*0.1))
else:
    print(amt-(amt*0.15))
'''------------------------------------------------------------------------'''
#9)ATM PIN VERIFICATION WITH BLOCKING LOGIC
stored_pin=1234
n=3
for i in range(n):
    p=int(input('Enter pin: '))
    if p==stored_pin:
        print('Access Granted')
        break
else:
    print("Atm Blocked.Try Again Later")
'''------------------------------------------------------------------------'''
#10)BUS BOOKING SYSTEM-TRACK FULL AND EMPTY SEATS
tot_seats=int(input())
booked_seats=list(map(int,input().split()))
print(f'Total Seats:{tot_seats}')
print(f'Booked:{len(booked_seats)}')
print(f'Available:{tot_seats-len(booked_seats)}')





