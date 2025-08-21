from ASSIGNMENT_5 import *   # Importing all classes (Train, ECTrain, PassengerDetails, Status, etc.)

# ----------------------- DATA SETUP -----------------------
# List of normal train names
train_names = ['hyderabad express', 'chennai superfast', 'delhi rajdhani', 'mumbai shatabdi',
               'bangalore intercity', 'kolkata duronto', 'pune express', 'ahmedabad garib rath',
               'lucknow mail', 'patna sampark kranti', 'secunderabad jan shatabdi',
               'jaipur double decker', 'bhubaneswar express', 'trivandrum kerala express',
               'goa mandovi express', 'varanasi express', 'nagpur duronto',
               'mysore express', 'coimbatore intercity', 'guwahati express']

# Dictionary storing details for each train (train_no, journeys, seats, ticket prices by class)
trains_available = {
    "hyderabad express": {"train_no": 17001, "journeys": "hyd to vskp", "seats_available": 120,
                          "ticket_price": {"2S": 120, "SL": 180, "3A": 360, "2A": 540, "1A": 840}},
    "chennai superfast": {"train_no": 12601, "journeys": "chennai to bangalore", "seats_available": 150,
                          "ticket_price": {"2S": 100, "SL": 160, "3A": 340, "2A": 500, "1A": 800}}
}
    # ... (other trains follow same structure)

# List of ECTrain names
EC_train_names = [
    "vande bharat express", "amrit bharat express", "howrah rajdhani express", "mumbai rajdhani express",
    "bhopal shatabdi express", "kalka shatabdi express", "sealdah duronto express", "mumbai duronto express"
]

# Dictionary for ECTrains (same structure but larger seat capacity)
EC_trains_available = {
    "vande bharat express": {"train_no": 22435, "journeys": "ndls to bsb", "seats_available": 1128,
                              "ticket_price": {"2S": 400, "SL": 600, "3A": 1200, "2A": 1800, "1A": 2800}},
    "amrit bharat express": {"train_no": 22436, "journeys": "ndls to bpl", "seats_available": 980,
                              "ticket_price": {"2S": 380, "SL": 560, "3A": 1100, "2A": 1700, "1A": 2600}}
}

    # ... (other EC trains follow)

# ----------------------- INITIALIZATION -----------------------
s = Status()   # Shared Status object to track bookings/cancellations
p = None       # Will store PassengerDetails object (last passenger reference for cancellation)
l = []         # List to store names of passengers who booked normal trains
l1 = []        # List to store names of passengers who booked EC trains

# ----------------------- MENU LOOP -----------------------
while True:
    # Display menu options
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

    ch = int(input("Enter your choice: "))   # User input
    if ch == 0:
        break   # Exit program

    # ------------------ BOOKING ------------------
    elif ch == 1:
        train_name = input("Enter train name: ").lower()
        journey = input("Enter journey (eg:- hyd to vskp): ").lower()

        # Booking for Normal Trains
        if (train_name in train_names and journey in trains_available[train_name]['journeys'] and
            trains_available[train_name]['seats_available'] > 0):

            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            reservation_choice = input("Enter your reservation choice(2S/SL/1A/2A/3A): ")

            # Validation: name should be unique, only letters/spaces, reservation choice valid
            if name not in l and all(i.isalpha() or i.isspace() for i in name) and reservation_choice in trains_available[train_name]['ticket_price']:
                t = Train(train_name, trains_available[train_name]['train_no'], trains_available[train_name]['seats_available'])
                p = PassengerDetails(name, age, reservation_choice, t, s)
                print(p.book_tickets(journey))   # Book ticket and print status
                # Update seat availability in dictionary
                trains_available[train_name]['seats_available'] = t.seats_avail
            else:
                print("Invalid/Repetitive Input of Name/Reservation Choice")
            l.append(name)

        # Booking for EC Trains
        elif (train_name in EC_train_names and journey in EC_trains_available[train_name]['journeys'] and
              EC_trains_available[train_name]['seats_available'] > 0):

            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            reservation_choice = input("Enter your reservation choice(2S/SL/1A/2A/3A): ")

            # Validation similar to normal trains
            if name not in l and all(ch.isalpha() or ch.isspace() for ch in name) and reservation_choice in trains_available[train_name]['ticket_price']:
                e = ECTrain(train_name, EC_trains_available[train_name]['train_no'], EC_trains_available[train_name]['seats_available'])
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
            jr = input('Enter the journey you booked: ')
            if p.cancel_ticket(jr):
                # Refund calculated based on ticket price of booked class
                print(f'Total Refund: {PassengerDetails.Tot_Ticket_Price_Booked(PassengerDetails.ticket_c(),trains_available[train_name]["ticket_price"][p.reservation_choice])}')
            else:
                print("No tickets booked to cancel")
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
        if p.reservation_choice in trains_available[train_name]['ticket_price']:
            print(f'Total money Spent: {PassengerDetails.Tot_Ticket_Price_Booked(PassengerDetails.ticket(),trains_available[train_name]["ticket_price"][p.reservation_choice])}')

    # ------------------ TRAIN DETAILS ------------------
    elif ch == 5:
        train_name = input("Enter train name: ")
        t = Train(train_name, trains_available[train_name]['train_no'], trains_available[train_name]['seats_available'],
                  trains_available[train_name]['journeys'])
        print(t.get_details())

    # ------------------ EC TRAIN DETAILS ------------------
    elif ch == 6:
        EC_train_name = input("Enter EC Train name: ")
        e = ECTrain(EC_train_name, EC_trains_available[EC_train_name]['train_no'], EC_trains_available[EC_train_name]['seats_available'],
                    EC_trains_available[EC_train_name]['journeys'])
        print(e.get_details())

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