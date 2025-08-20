from ASSIGNMENT_5 import *

train_names = ['hyderabad express', 'chennai superfast', 'delhi rajdhani', 'mumbai shatabdi',
               'bangalore intercity', 'kolkata duronto', 'pune express', 'ahmedabad garib rath',
               'lucknow mail', 'patna sampark kranti', 'secunderabad jan shatabdi',
               'jaipur double decker', 'bhubaneswar express', 'trivandrum kerala express',
               'goa mandovi express', 'varanasi express', 'nagpur duronto',
               'mysore express', 'coimbatore intercity', 'guwahati express']

trains_available = {
    "hyderabad express": {"train_no": 17001, "journeys": "hyd to vskp", "seats_available": 120, "ticket_price": {"2S": 120, "SL": 180, "3A": 360, "2A": 540, "1A": 840}},
    "chennai superfast": {"train_no": 12601, "journeys": "mas to sbc", "seats_available": 85, "ticket_price": {"2S": 100, "SL": 150, "3A": 300, "2A": 450, "1A": 700}},
    "delhi rajdhani": {"train_no": 12431, "journeys": "ndls to bct", "seats_available": 40, "ticket_price": {"2S": 500, "SL": 750, "3A": 1500, "2A": 2250, "1A": 3500}},
    "mumbai shatabdi": {"train_no": 12009, "journeys": "bct to adi", "seats_available": 60, "ticket_price": {"2S": 200, "SL": 300, "3A": 600, "2A": 900, "1A": 1400}},
    "bangalore intercity": {"train_no": 12677, "journeys": "sbc to mas", "seats_available": 95, "ticket_price": {"2S": 150, "SL": 225, "3A": 450, "2A": 675, "1A": 1050}},
    "kolkata duronto": {"train_no": 12245, "journeys": "hwh to ndls", "seats_available": 75, "ticket_price": {"2S": 450, "SL": 675, "3A": 1350, "2A": 2025, "1A": 3150}},
    "pune express": {"train_no": 12129, "journeys": "pune to bct", "seats_available": 110, "ticket_price": {"2S": 120, "SL": 180, "3A": 360, "2A": 540, "1A": 840}},
    "ahmedabad garib rath": {"train_no": 12909, "journeys": "adi to ndls", "seats_available": 150, "ticket_price": {"2S": 160, "SL": 240, "3A": 480, "2A": 720, "1A": 1120}},
    "lucknow mail": {"train_no": 12229, "journeys": "lko to ndls", "seats_available": 55, "ticket_price": {"2S": 140, "SL": 210, "3A": 420, "2A": 630, "1A": 980}},
    "patna sampark kranti": {"train_no": 12393, "journeys": "pnbe to ndls", "seats_available": 90, "ticket_price": {"2S": 150, "SL": 225, "3A": 450, "2A": 675, "1A": 1050}},
    "secunderabad jan shatabdi": {"train_no": 12079, "journeys": "sc to bza", "seats_available": 100, "ticket_price": {"2S": 90, "SL": 135, "3A": 270, "2A": 405, "1A": 630}},
    "jaipur double decker": {"train_no": 12985, "journeys": "jp to ndls", "seats_available": 80, "ticket_price": {"2S": 170, "SL": 255, "3A": 510, "2A": 765, "1A": 1190}},
    "bhubaneswar express": {"train_no": 12893, "journeys": "bbs to hwh", "seats_available": 65, "ticket_price": {"2S": 80, "SL": 120, "3A": 240, "2A": 360, "1A": 560}},
    "trivandrum kerala express": {"train_no": 12625, "journeys": "tvc to ndls", "seats_available": 130, "ticket_price": {"2S": 250, "SL": 375, "3A": 750, "2A": 1125, "1A": 1750}},
    "goa mandovi express": {"train_no": 10103, "journeys": "mao to bct", "seats_available": 70, "ticket_price": {"2S": 100, "SL": 150, "3A": 300, "2A": 450, "1A": 700}},
    "varanasi express": {"train_no": 14235, "journeys": "bsb to lko", "seats_available": 45, "ticket_price": {"2S": 60, "SL": 90, "3A": 180, "2A": 270, "1A": 420}},
    "nagpur duronto": {"train_no": 12289, "journeys": "ngp to bct", "seats_available": 50, "ticket_price": {"2S": 400, "SL": 600, "3A": 1200, "2A": 1800, "1A": 2800}},
    "mysore express": {"train_no": 16231, "journeys": "mys to sbc", "seats_available": 115, "ticket_price": {"2S": 80, "SL": 120, "3A": 240, "2A": 360, "1A": 560}},
    "coimbatore intercity": {"train_no": 12679, "journeys": "cbe to mas", "seats_available": 105, "ticket_price": {"2S": 100, "SL": 150, "3A": 300, "2A": 450, "1A": 700}},
    "guwahati express": {"train_no": 15645, "journeys": "ghy to hwh", "seats_available": 90, "ticket_price": {"2S": 200, "SL": 300, "3A": 600, "2A": 900, "1A": 1400}}
}


EC_train_names = [
    "vande bharat express", "amrit bharat express", "howrah rajdhani express", "mumbai rajdhani express",
    "bhopal shatabdi express", "kalka shatabdi express", "sealdah duronto express", "mumbai duronto express"
]

EC_trains_available = {
    "vande bharat express": {"train_no": 22435, "journeys": ["ndls to bsb", "ndls to svdk", "bct to gnr"], "seats_available": 1128, "ticket_price": {"2S": 400, "SL": 600, "3A": 1200, "2A": 1800, "1A": 2800}},
    "amrit bharat express": {"train_no": 22441, "journeys": "ndls to gkp", "seats_available": 1200, "ticket_price": {"2S": 350, "SL": 525, "3A": 1050, "2A": 1575, "1A": 2450}},
    "howrah rajdhani express": {"train_no": 12301, "journeys": "hwh to ndls", "seats_available": 1300, "ticket_price": {"2S": 450, "SL": 675, "3A": 1350, "2A": 2025, "1A": 3150}},
    "mumbai rajdhani express": {"train_no": 12951, "journeys": "bct to ndls", "seats_available": 1250, "ticket_price": {"2S": 480, "SL": 720, "3A": 1440, "2A": 2160, "1A": 3360}},
    "bhopal shatabdi express": {"train_no": 12001, "journeys": "ndls to bpl", "seats_available": 850, "ticket_price": {"2S": 300, "SL": 450, "3A": 900, "2A": 1350, "1A": 2100}},
    "kalka shatabdi express": {"train_no": 12005, "journeys": "ndls to klk", "seats_available": 700, "ticket_price": {"2S": 320, "SL": 480, "3A": 960, "2A": 1440, "1A": 2240}},
    "sealdah duronto express": {"train_no": 12259, "journeys": "sda to ndls", "seats_available": 950, "ticket_price": {"2S": 400, "SL": 600, "3A": 1200, "2A": 1800, "1A": 2800}},
    "mumbai duronto express": {"train_no": 12261, "journeys": "bct to hwh", "seats_available": 1000, "ticket_price": {"2S": 420, "SL": 630, "3A": 1260, "2A": 1890, "1A": 2940}}
}


# Shared status object
s = Status()
p = None  # keep global passenger reference for cancellation
l=[]
l1=[]
while True:
    print('''
0: "Exit"      
1: "Booking"
2: "Cancelling and Refund Information"
3: "View Transactions"
4: "Total Money Spent"
5: "Train Details"
6: "ECTrain Details"
7: "List of your names used during booking"
8: "Main Services Provided"          
''')
    ch = int(input("Enter your choice: "))
    if ch == 0:
        break

    elif ch == 1:
        train_name = input("Enter train name: ").lower()
        journey = input("Enter journey (eg:- hyd to vskp): ").lower()

        # Normal trains
        if (train_name in train_names and journey in trains_available[train_name]['journeys'] and
            trains_available[train_name]['seats_available'] > 0):

            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            reservation_choice = input("Enter your reservation choice(2S/SL/1A/2A/3A): ")
            if name not in l and all(i.isalpha() or i.isspace() for i in name) and reservation_choice in trains_available[train_name]['ticket_price']:
                t = Train(train_name, trains_available[train_name]['train_no'], trains_available[train_name]['seats_available'])
                p = PassengerDetails(name, age, reservation_choice, t, s)
                print(p.book_tickets(journey))
                    # update dictionary
                trains_available[train_name]['seats_available'] = t.seats_avail
            else:
                print("Invalid/Repetetive Input of Name/Reservation Choice")
            l.append(name)
        # EC trains
        elif (train_name in EC_train_names and journey in EC_trains_available[train_name]['journeys'] and
              EC_trains_available[train_name]['seats_available'] > 0):
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            reservation_choice = input("Enter your reservation choice(2S/SL/1A/2A/3A): ")
            if name not in l and all(ch.isalpha() or ch.isspace() for ch in name) and reservation_choice in trains_available[train_name]['ticket_price']:
                e = ECTrain(train_name, EC_trains_available[train_name]['train_no'], EC_trains_available[train_name]['seats_available'])
                p = PassengerDetails(name, age, reservation_choice, e, s)
                print(p.book_tickets(journey))
                # update dictionary
                EC_trains_available[train_name]['seats_available'] = e.seats_avail
            else:
                print("Invalid input of name/reservation choice")
            l1.append(name)
    elif ch == 2:
        if p:
            jr=input('Enter the journey you booked: ')
            if p.cancel_ticket(jr):
                print(f'Total Refund: {PassengerDetails.Tot_Ticket_Price_Booked(PassengerDetails.ticket_c(),trains_available[train_name]['ticket_price'][p.reservation_choice])}')
            else:
                print("No tickets booked to cancel")
        else:
            print('No tickets cancelled')
        
    elif ch==3:
        if p:
            print(f'History:{p.train_history()}')
        else:
            print("No Booking/cancelled History")

    elif ch==4:
        if p.reservation_choice in trains_available[train_name]['ticket_price']:
            print(f'Total money Spent: {PassengerDetails.Tot_Ticket_Price_Booked(PassengerDetails.ticket(),trains_available[train_name]['ticket_price'][p.reservation_choice])}')
    
    elif ch == 5:
        train_name = input("Enter train name: ")
        t = Train(train_name, trains_available[train_name]['train_no'], trains_available[train_name]['seats_available'],
                  trains_available[train_name]['journeys'])
        print(t.get_details())

    elif ch == 6:
        EC_train_name = input("Enter EC Train name: ")
        e = ECTrain(EC_train_name, EC_trains_available[EC_train_name]['train_no'], EC_trains_available[EC_train_name]['seats_available'],
                    EC_trains_available[EC_train_name]['journeys'])
        print(e.get_details())
    elif ch == 7:
        print(f'List of your names:{PassengerDetails.passenger_count(s.passengers_name)}')
    elif ch==8:
        print(f'Main Works are: {Train.service()}')
    else:
        print("Invalid Choice")
    

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