#SWIGGY
data={
      'gopi@gmail.com':'Gopi@1234',
      'venkat@gmail.com':'venky@1234',
      'Charansai@gmail.com':'Chass@1234',
      }
email,pwd=input('Enter the email and password: ').split()
if email in data and pwd == data[email]: #if data[email] == pwd:
    print("Login Successful")
else:
    print("Invalid Login")


data = {
    'gopi@gmail.com': 'Gopi@1234',
    'venkat@gmail.com': 'venky@1234',
    'Charansai@gmail.com': 'Chass@1234',
}

email, pwd = input('Enter the email and password: ').split() 
if data.get(email) == pwd: #(BETTER OPTION)-For Not Getting Errors
    print("login Successful")
else:
    print("Invalid Login")
'''-------------------------------------------------------------------------------------------------------------'''
items=['coffee','icecream','samosa','idly']
data=input("Enter the item: ")
if data in items:
    print("Available")
else:
    print("Not Available")
############################
items=['coffee','icecream','samosa','idly']
stocks=[20,50,40,0]    
if data in items:
    ind=items.index(data)
    if stocks[ind]>0:
        print("Available",stocks[ind])
    else:
        print("Out of stock.please try again")
else:
    print("Item NA")
'''-------------------------------------------------------------------------------------------------------------'''
items=['coffee','icecream','samosa','idly']
distance=[13,4,9,12]
rating=[3.2,4.4,3,1]
cost=[150,60,20,40]
veg_status=[True,True,False,True]
time=[40,35,25,15]
data=input("Enter the item: ")
ind=items.index(data)
if distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg_status[ind] and time[ind]<30:
    print('All Filters Applied')
elif distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg_status[ind]:
    print("Distance and rating and cost and veg_status applied")
elif distance[ind]<5 and rating[ind]>4 and cost[ind]<500:
    print("Distance and rating and cost applied")
elif distance[ind]<5 and rating[ind]>4:
    print("Distance and rating applied")
elif distance[ind]<5:
    print("Distance applied")
else:
    print("Show all products")
'''-------------------------------------------------------------------------------------------------------------'''
num=int(input("Enter the num: "))
if num%2==0 and num%3==0:
    print('Divisible by 2 and 3')
elif num%2==0:
    print('Divisible by 2')
elif num%3==0:
    print("Divisible by 3")
else:
    print("Not Divisible by 2 or 3")
'''-------------------------------------------------------------------------------------------------------------'''
year=int(input("Enter the num: "))
if year%400==0 or (year%4==0 and year%100!=0):
         print("Leap yr")
         
