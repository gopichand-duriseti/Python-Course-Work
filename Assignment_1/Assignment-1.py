###################### IRCTC TRAIN ######################
import random
Book_Tickets=list(input("Enter the ticket: "))
Cancel_Ticket=tuple(input("Enter the tickets to be cancelled: ").split()) 
PNR_Enquiry=int(input("Enter PNR number: "))
File_TDR=input("Select The Booked Ticket to File TDR: ")
FAQ=input("Enter FAQ: ").split()
Track_Train=input("Enter the Train Name to track: ")
location=set(input("Enter Locations: ").split())
year_2025_booking_percent_TATKAL=float(input("Enter the percentage: "))
Total_Tickets_P1_P2=eval(input('Enter Total passengers("P_num:total") '))

#Printing Booked Tickets
print(f"The booked tickets are {Book_Tickets}")

#Printing the tickets that are cancelled
print(f"The cancelled tickets are {Cancel_Ticket}")

#Knowing the details of your PNR Number
print("Your {} PNR Number number details are: ".format(PNR_Enquiry))

#To see/observe the frequently asked questions
print("Frequently Asked Questions related to train are",FAQ)

#See the ticket you Filed the TDR due to ticket cancellation/train delays
print("The ticket you filed a TDR is given below\n%s"%(File_TDR))

#Tracking the location of Train
print(f"The Train location is at {location} locations")

#2025 bookings in percentage in tatkal
print("The total bookings of tatkal in 2025 in percentage is %.1f"%(year_2025_booking_percent_TATKAL))
