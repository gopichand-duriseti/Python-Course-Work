from ASSIGNMENT_5 import *   # Importing all classes (Train, ECTrain, PassengerDetails, Status, etc.)

# ----------------------- DATA SETUP -----------------------
# List of normal train names
train_names = [
    '1.hyderabad express (hyd to mas)','2.chennai superfast (mas to sbc)'
]


# Dictionary storing details for each train (train_no, journeys, seats, ticket prices by class)
trains_available = {
    1: {"name": "hyderabad express", "train_no": 17001, "journeys": "hyd to mas", "seats_available": 120,
        "ticket_price": {"2S": 120, "SL": 180, "3A": 360, "2A": 540, "1A": 840}},
    2: {"name": "chennai superfast", "train_no": 12601, "journeys": "mas to sbc", "seats_available": 150,
        "ticket_price": {"2S": 100, "SL": 160, "3A": 340, "2A": 500, "1A": 800}}
}

    # ... (other trains follow same structure)

# List of ECTrain names
ec_train_names = [
    "1.vande bharat express (ndls to bsb)","2.amrit bharat express (pnbe to ndls)"
]

# Dictionary for ECTrains (same structure but larger seat capacity)
EC_trains_available = {
    1: {"name": "vande bharat express", "train_no": 22435, "journeys": "ndls to bsb", "seats_available": 1128,
        "ticket_price": {"2S": 400, "SL": 600, "3A": 1200, "2A": 1800, "1A": 2800}},
    2: {"name": "amrit bharat express", "train_no": 22436, "journeys": "pnbe to ndls", "seats_available": 980,
        "ticket_price": {"2S": 380, "SL": 560, "3A": 1100, "2A": 1700, "1A": 2600}}
}


    # ... (other EC trains follow)

# ----------------------- INITIALIZATION -----------------------
s = Status()   # Shared Status object to track bookings/cancellations
p = None       # Will store PassengerDetails object (last passenger reference for cancellation)
l = []         # List to store names of passengers who booked normal trains
l1 = []        # List to store names of passengers who booked EC trains
x,x1=0,0

# ----------------------- MENU LOOP -----------------------
while True:
    # Display menu options
    print()
    print('MENU:-',end='')
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
    print(f'train_names:{train_names}')
    print(f'EC_train_names:{ec_train_names}')

    ch = int(input("Enter your choice: "))   # User input
    if ch == 0:
        break   # Exit program

    # ------------------ BOOKING ------------------
    elif ch == 1:
        train_name_ch = int(input("select number for train from details give above: "))
        journey = input("Enter journey (eg:- hyd to vskp) related to the selected train: ").lower()

        # Booking for Normal Trains
        if (trains_available[train_name_ch]['name'] in train_names[train_name_ch-1] and journey in trains_available[train_name_ch]['journeys'] and
            trains_available[train_name_ch]['seats_available'] > 0):

            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            reservation_choice = input("Enter your reservation choice(2S/SL/1A/2A/3A): ")

            # Validation: name should be unique, only letters/spaces, reservation choice valid
            if name not in l and all(i.isalpha() or i.isspace() for i in name) and reservation_choice in trains_available[train_name_ch]['ticket_price']:
                t = Train(trains_available[train_name_ch]['name'], trains_available[train_name_ch]['train_no'], trains_available[train_name_ch]['seats_available'])
                p = PassengerDetails(name, age, reservation_choice, t, s)
                print(p.book_tickets(journey))   # Book ticket and print status
                # Update seat availability in dictionary
                trains_available[train_name_ch]['seats_available'] = t.seats_avail
            else:
                print("Invalid/Repetitive Input of Name/Reservation Choice")
            l.append(name)

        # Booking for EC Trains
        elif (EC_trains_available[train_name_ch]['name'] in ec_train_names[train_name_ch-1] and journey in EC_trains_available[train_name_ch]['journeys'] and
              EC_trains_available[train_name_ch]['seats_available'] > 0):

            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            reservation_choice = input("Enter your reservation choice(2S/SL/1A/2A/3A): ")

            # Validation similar to normal trains
            if name not in l1 and all(ch.isalpha() or ch.isspace() for ch in name) and reservation_choice in EC_trains_available[train_name_ch]['ticket_price']:
                e = ECTrain(EC_trains_available[train_name_ch]['name'], EC_trains_available[train_name_ch]['train_no'], EC_trains_available[train_name_ch]['seats_available'])
                p = PassengerDetails(name, age, reservation_choice, e, s)
                print(p.book_tickets(journey))
                # Update seat availability
                EC_trains_available[train_name]['seats_available'] = e.seats_avail
            else:
                print("Invalid input of name/reservation choice")
            l1.append(name)

    # ------------------ CANCELLATION ------------------
    elif ch == 2:
        if p:
            train_name_c=int(input("select Number for train/EC train from details give above to cancel: "))
            jr = input('Enter the journey you booked: ')
            try:
                # Refund calculated based on ticket price of booked class of Normal Train
                if p.cancel_ticket(jr) and jr in trains_available[train_name_c]['journeys']:
                    x=PassengerDetails.Tot_Ticket_Price_Booked(PassengerDetails.ticket(),trains_available[train_name_c]["ticket_price"][p.reservation_choice])
                    print(f'Total Refund(Normal Trains): {x}')
            except :
                # Refund calculated based on ticket price of booked class of EC Train
                x1=PassengerDetails.Tot_Ticket_Price_Booked(PassengerDetails.ticket_c(),EC_trains_available[train_name_c]["ticket_price"][p.reservation_choice])
                print(f'Total Refund(EC): {x1}')
            print(f'Total Refund Till now:{x+x1}')
        else:
            print('No tickets cancelled')
    

    # ------------------ VIEW TRANSACTION HISTORY ------------------
    elif ch == 3:
        if p:
            print(f'History:{p.train_history()}')
        else:
            print("No Booking/Cancelled History")

    # ------------------ TOTAL MONEY SPENT ------------------
    elif ch == 4:
        if p:
            if p.reservation_choice in trains_available[train_name_ch]['ticket_price']:
                print(f'Total money Spent: {PassengerDetails.Tot_Ticket_Price_Booked(PassengerDetails.ticket(),trains_available[train_name_ch]["ticket_price"][p.reservation_choice])}')
            else:
                print("Wrong input of reservation choice")
        else:
            print("You haven't spent/You got the money you spent")

    # ------------------ TRAIN DETAILS ------------------
    elif ch == 5:
        try:
            train_name = int(input("Enter given choice get the details of train: "))
            t = Train(trains_available[train_name]['name'], trains_available[train_name]['train_no'], trains_available[train_name]['seats_available'],
                  trains_available[train_name]['journeys'])
            print(t.get_details())
        except :
            print("Invalid Train name")
    # ------------------ EC TRAIN DETAILS ------------------
    elif ch == 6:
        try:
            EC_train_name = int(input("Enter given choice get te details of EC train: "))
            e = ECTrain(EC_trains_available[EC_train_name]['name'], EC_trains_available[EC_train_name]['train_no'], EC_trains_available[EC_train_name]['seats_available'],
                        EC_trains_available[EC_train_name]['journeys'])
            print(e.get_details())
        except :
            print("Invalid EC Train name")
    # ------------------ LIST OF NAMES ------------------
    elif ch == 7:
        print(f'List of your names:{PassengerDetails.passenger_count(s.passengers_name)}')

    # ------------------ MAIN SERVICES ------------------
    elif ch == 8:
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