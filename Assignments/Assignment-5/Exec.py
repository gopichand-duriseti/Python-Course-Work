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
l = []         # List to store names of passengers who booked trains
x,x1=0,0
x_a=[]
a,b=0,0
# ----------------------- MENU LOOP -----------------------
while True:
    # Display menu options
    print()
    print('MENU:-',end='')
    print('''
0: "Exit"      
1: "Booking"
2: "Cancelling and Refund Information"
3: "View History"
4: "Total Money Spent"
5: "Train Details"
6: "ECTrain Details"
7: "List of your names used during booking"
8: "Main Services Provided"     
9: "Total Money after booking and cancelling ticket"               
''')
    print(f'train_names:{train_names}')
    print(f'EC_train_names:{ec_train_names}')

    ch = int(input("Enter your choice: "))   # User input
    if ch == 0:
        break   # Exit program

    # ------------------ BOOKING ------------------
    elif ch == 1:
        train_name_ch = int(input("select number for train from details given above: "))
        journey = input("Enter journey (eg:- hyd to mas) related to the selected train: ").lower()

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
                a=PassengerDetails.Tot_Ticket_Price_Booked(PassengerDetails.ticket(),trains_available[train_name_ch]["ticket_price"][p.reservation_choice])
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
            if name not in l and all(ch.isalpha() or ch.isspace() for ch in name) and reservation_choice in EC_trains_available[train_name_ch]['ticket_price']:
                e = ECTrain(EC_trains_available[train_name_ch]['name'], EC_trains_available[train_name_ch]['train_no'], EC_trains_available[train_name_ch]['seats_available'])
                p = PassengerDetails(name, age, reservation_choice, e, s)
                print(p.book_tickets(journey))
                # Update seat availability
                EC_trains_available[train_name_ch]['seats_available'] = e.seats_avail
                b=PassengerDetails.Tot_Ticket_Price_Booked(PassengerDetails.ticket(),EC_trains_available[train_name_ch]["ticket_price"][p.reservation_choice])
                print(a,b)
            else:
                print("Invalid/Repetitive Input of Name/Reservation Choice")
            l.append(name)

    # ------------------ CANCELLATION ------------------
    elif ch == 2:
        if p:
            train_name_c=int(input("select Number for train/EC train from details give above to cancel: "))
            jr = input('Enter the journey you booked: ')
            # Refund calculated based on ticket price of booked class of Normal Train
            if p.cancel_ticket(jr) and jr in trains_available[train_name_c]['journeys']:
                x=PassengerDetails.Tot_Ticket_Price_Cancelled(PassengerDetails.ticket(),trains_available[train_name_c]["ticket_price"][p.reservation_choice])
                print(f'Total Refund(Normal Trains): {abs(x)}')
            else:
                x1=PassengerDetails.Tot_Ticket_Price_Cancelled(PassengerDetails.ticket(),EC_trains_available[train_name_c]["ticket_price"][p.reservation_choice])
                print(f'Total Refund(EC): {abs(x1)}')
            print(f'Total Refund Till now: {abs(x+x1)}')
            x_a.append(abs(x+x1))
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
            tot=a+b
            print(tot)
        else:
            print("You haven't spent/You got the money you spent through refund policy")

    # ------------------ TRAIN DETAILS ------------------
    elif ch == 5:
        try:
            train_name_no = int(input("Enter given choice get the details of train: "))
            t = Train(trains_available[train_name_no]['name'], trains_available[train_name_no]['train_no'], trains_available[train_name_no]['seats_available'],
                  trains_available[train_name_no]['journeys'])
            print(t.get_details())
        except :
            print("Invalid Train name")
    # ------------------ EC TRAIN DETAILS ------------------
    elif ch == 6:
        try:
            EC_train_name= int(input("Enter given choice get te details of EC train: "))
            e = ECTrain(EC_trains_available[EC_train_name]['name'], EC_trains_available[EC_train_name]['train_no'], EC_trains_available[EC_train_name]['seats_available'],
                        EC_trains_available[EC_train_name]['journeys'])
            print(e.get_details())
        except :
            print("Invalid EC Train name")
    # ------------------ LIST OF NAMES ------------------
    elif ch == 7:
        l_n=PassengerDetails.passenger_names(s.passengers_name)
        if l_n:
            print(f'List of your names:{l_n}')
        else:
            print("No Names saved.")

    # ------------------ MAIN SERVICES ------------------
    elif ch == 8:
        print(f'Main Services Provided are: {Train.service()}')
    # ------------------ TOTAL MONEY AFTER BOOKING AND CANCELLING
    elif ch==9:
        print(f'Total Money after booking and cancelling:{PassengerDetails.difference(tot-sum(x_a))}')

    else:
        print("Invalid Choice")