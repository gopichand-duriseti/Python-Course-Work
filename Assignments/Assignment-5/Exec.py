from ASSIGNMENT_5 import *

#Cost should be checked by considering train and reservation choice
print('''
0: "Enter your Details to book ticket"
1: "Booking"
2: "Cancelling"
3: "View Transactions"
4: "Total Money Gain/Loss"
''')
ch=int(input("Enter your choice: "))
train_names=['hyderabad express', 'chennai superfast', 'delhi rajdhani', 'mumbai shatabdi', 
 'bangalore intercity', 'kolkata duronto', 'pune express', 'ahmedabad garib rath', 
 'lucknow mail', 'patna sampark kranti', 'secunderabad jan shatabdi', 
 'jaipur double decker', 'bhubaneswar express', 'trivandrum kerala express', 
 'goa mandovi express', 'varanasi express', 'nagpur duronto', 
 'mysore express', 'coimbatore intercity', 'guwahati express']


trains_available = {
    "hyderabad express": {"journeys": "hyd to vskp", "seats_available": 120},
    "chennai superfast": {"journeys": "mas to sbc", "seats_available": 85},
    "delhi rajdhani": {"journeys": "ndls to bct", "seats_available": 40},
    "mumbai shatabdi": {"journeys": "bct to adi", "seats_available": 60},
    "bangalore intercity": {"journeys": "sbc to mas", "seats_available": 95},
    "kolkata duronto": {"journeys": "hwh to ndls", "seats_available": 75},
    "pune express": {"journeys": "pune to bct", "seats_available": 110},
    "ahmedabad garib rath": {"journeys": "adi to ndls", "seats_available": 150},
    "lucknow mail": {"journeys": "lko to ndls", "seats_available": 55},
    "patna sampark kranti": {"journeys": "pnbe to ndls", "seats_available": 90},
    "secunderabad jan shatabdi": {"journeys": "sc to bza", "seats_available": 100},
    "jaipur double decker": {"journeys": "jp to ndls", "seats_available": 80},
    "bhubaneswar express": {"journeys": "bbs to hwh", "seats_available": 65},
    "trivandrum kerala express": {"journeys": "tvc to ndls", "seats_available": 130},
    "goa mandovi express": {"journeys": "mao to bct", "seats_available": 70},
    "varanasi express": {"journeys": "bsb to lko", "seats_available": 45},
    "nagpur duronto": {"journeys": "ngp to bct", "seats_available": 50},
    "mysore express": {"journeys": "mys to sbc", "seats_available": 115},
    "coimbatore intercity": {"journeys": "cbe to mas", "seats_available": 105},
    "guwahati express": {"journeys": "ghy to hwh", "seats_available": 90}
}



if ch==1:
    train_name=input("Enter train name: ").lower()
    journey=input("Enter train number(eg:-hyd to vskp): ") .lower()
    if train_name in train_names and journey in trains_available[train_name]['journeys'] and trains_available[train_name]['seats_available']>0:
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        reservation_choice=input("Enter your reservation choice: ")
        t=Train(train_name,journey,trains_available[train_name]['seats_available'])
        p=PassengerDetails(name,age,reservation_choice,t)
        print(p.book_tickets(journey))
elif ch==2:
    pass
    #p=PassengerDetails(name,age,reservation_choice,t)
    #print(p.cancel_ticket(input('Enter the journey you booked: ')))

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