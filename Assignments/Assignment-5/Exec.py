from ASSIGNMENT_5 import *

#Cost should be checked by considering train and reservation choice
print('''
0: "Exit"      
1: "Booking"
2: "Cancelling"
3: "View Transactions"
4: "Total Money Gain/Loss"
5: "Train Details"
6: "ECTrain Details"      
''')

train_names=['hyderabad express', 'chennai superfast', 'delhi rajdhani', 'mumbai shatabdi', 
 'bangalore intercity', 'kolkata duronto', 'pune express', 'ahmedabad garib rath', 
 'lucknow mail', 'patna sampark kranti', 'secunderabad jan shatabdi', 
 'jaipur double decker', 'bhubaneswar express', 'trivandrum kerala express', 
 'goa mandovi express', 'varanasi express', 'nagpur duronto', 
 'mysore express', 'coimbatore intercity', 'guwahati express']


trains_available = {
    "hyderabad express": {"train_no": 17001, "journeys": "hyd to vskp", "seats_available": 120},
    "chennai superfast": {"train_no": 12601, "journeys": "mas to sbc", "seats_available": 85},
    "delhi rajdhani": {"train_no": 12431, "journeys": "ndls to bct", "seats_available": 40},
    "mumbai shatabdi": {"train_no": 12009, "journeys": "bct to adi", "seats_available": 60},
    "bangalore intercity": {"train_no": 12677, "journeys": "sbc to mas", "seats_available": 95},
    "kolkata duronto": {"train_no": 12245, "journeys": "hwh to ndls", "seats_available": 75},
    "pune express": {"train_no": 12129, "journeys": "pune to bct", "seats_available": 110},
    "ahmedabad garib rath": {"train_no": 12909, "journeys": "adi to ndls", "seats_available": 150},
    "lucknow mail": {"train_no": 12229, "journeys": "lko to ndls", "seats_available": 55},
    "patna sampark kranti": {"train_no": 12393, "journeys": "pnbe to ndls", "seats_available": 90},
    "secunderabad jan shatabdi": {"train_no": 12079, "journeys": "sc to bza", "seats_available": 100},
    "jaipur double decker": {"train_no": 12985, "journeys": "jp to ndls", "seats_available": 80},
    "bhubaneswar express": {"train_no": 12893, "journeys": "bbs to hwh", "seats_available": 65},
    "trivandrum kerala express": {"train_no": 12625, "journeys": "tvc to ndls", "seats_available": 130},
    "goa mandovi express": {"train_no": 10103, "journeys": "mao to bct", "seats_available": 70},
    "varanasi express": {"train_no": 14235, "journeys": "bsb to lko", "seats_available": 45},
    "nagpur duronto": {"train_no": 12289, "journeys": "ngp to bct", "seats_available": 50},
    "mysore express": {"train_no": 16231, "journeys": "mys to sbc", "seats_available": 115},
    "coimbatore intercity": {"train_no": 12679, "journeys": "cbe to mas", "seats_available": 105},
    "guwahati express": {"train_no": 15645, "journeys": "ghy to hwh", "seats_available": 90}
}

EC_train_names = [
    "vande bharat express","amrit bharat express","howrah rajdhani exprss","mumbai rajdhani express","bhopal shatabdi express",
    "kalka shatabdi express","sealdah duronto express","mumbai duronto express"
]


EC_trains_available = {
    "vande bharat express": {
        "train_no": 22435,
        "journeys": ["ndls to bsb", "ndls to svdk", "bct to gnr", "mas to mys", "sc to vskp"],
        "seats_available": 1128
    },
    "amrit bharat express": {"train_no": 22441, "journeys": "ndls to gkp", "seats_available": 1200},
    "howrah rajdhani express": {"train_no": 12301, "journeys": "hwh to ndls", "seats_available": 1300},
    "mumbai rajdhani express": {"train_no": 12951, "journeys": "bct to ndls", "seats_available": 1250},
    "bhopal shatabdi express": {"train_no": 12001, "journeys": "ndls to bpl", "seats_available": 850},
    "kalka shatabdi express": {"train_no": 12005, "journeys": "ndls to klk", "seats_available": 700},
    "sealdah duronto express": {"train_no": 12259, "journeys": "sda to ndls", "seats_available": 950},
    "mumbai duronto express": {"train_no": 12261, "journeys": "bct to hwh", "seats_available": 1000}
}

while True:
    ch=int(input("Enter your choice: "))
    if ch==0:
        break
    elif ch==1:
        train_name=input("Enter train name: ").lower()
        journey=input("Enter train number(eg:-hyd to vskp): ") .lower()
        if train_name in train_names and journey in trains_available[train_name]['journeys'] and trains_available[train_name]['seats_available']>0:
            name=input("Enter your name: ")
            age=int(input("Enter your age: "))
            reservation_choice=input("Enter your reservation choice: ")
            t=Train(train_name,journey,trains_available[train_name]['seats_available'])
            p=PassengerDetails(name,age,reservation_choice,t)
            print(p.book_tickets(journey))
        elif train_name in EC_train_names and journey in EC_trains_available[train_name]['journeys'] and EC_trains_available[train_name]['seats_available']>0:
            name=input("Enter your name: ")
            age=int(input("Enter your age: "))
            reservation_choice=input("Enter your reservation choice: ")
            e=ECTrain(train_name,journey,EC_trains_available[train_name]['seats_available'])
            p=PassengerDetails(name,age,reservation_choice,e)
            print(p.book_tickets(journey))
    elif ch==2:
        print(p.cancel_ticket(input('Enter the journey you booked: ')))
    elif ch==5:
        train_name=input("Enter train name: ")
        t=Train(train_name,trains_available[train_name]['train_no'],trains_available[train_name]['seats_available'],
                trains_available[train_name]['journeys'])
        print(t.get_details())
    elif ch==6:
        EC_train_name=input("Enter EC Train name: ")
        e=ECTrain(EC_train_name,EC_trains_available[EC_train_name]['train_no'],EC_trains_available[EC_train_name]['seats_available'],
                EC_trains_available[EC_train_name]['journeys'])
        print(e.get_details())
    elif ch==7:
        p=PassengerDetails()
        print(p.passenger_count(p.status.passengers_name))
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