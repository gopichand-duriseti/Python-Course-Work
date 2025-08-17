from ASSIGNMENT_5 import *

#Cost should be checked by considering train and reservation choice
print('''
0: "Enter your Details to book ticket"
1: "Booking"
2: "Cancelling"
3: "View Transactions"
4: "Total Money Gain/Loss"
''')
ch=int(input("Enter your Choice: "))
train_name=input("Enter train name: ")
train_no=int(input("Enter train no: "))
seats_avail=int(input("Enter seats_avail: "))
t=Train(train_name,train_no,seats_avail)
if ch==0:
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    reservation_choice=input("Enter your reservation choice: ")
if ch==1:
    p=PassengerDetails(name,age,reservation_choice,t)
    print(p.book_tickets(input("Enter your journey: ")))
    print(p.book_tickets(input('Enter your journey: ')))
elif ch==2:
    p=PassengerDetails(name,age,reservation_choice,t)
    print(p.cancel_ticket(input('Enter the journey you booked: ')))

'''c=EVTrain("hello",123456,23,1000)
print(c.get_details())
print(c.service())
p=PassengerDetails('gopi',23,'2s',t)
print(p.book_tickets('Hyd-Vij'))
print(p.book_tickets('Hy-Vij'))
print(p.cancel_ticket('Hyd-Vij'))
print(p.passenger_count(p.status.passengers_name))
tot_amt=p.Tot_Ticket_Price_Booked(p.status.booked,167)
tot_amt_canc=p.Tot_Ticket_Price_Booked(p.status.cancelled,167)
print(f'Total amount after booking and cancellation:{tot_amt-tot_amt_canc}')
'''