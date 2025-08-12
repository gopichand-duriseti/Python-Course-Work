#TRAIN
#service=online #class variable
#ECTRAIN(TRAIN) #Inheritance
#name,age,seats_available(attributes)---_name(protected),__seats_available(private),age(public) #encapsulation
#Book_Ticket and Cancel_Ticket(Methods)---Instance method
#display_details(self)---related to train
#display_details(self)---related to ectrain #polymorphism
#@classmethod #def servicing(cls):return cls.service---class method
#@staticmethod #if __seats_available>0
print("IRCTC".center(100,"-"))
class Train:
    services=['Train Booking','Cancelling Train Ticket']
    def __init__(self,train_name,train_no,seats_avail):
        self.train_name=train_name
        self.train_no=train_no
        self.__seats_avail=seats_avail
    def seats(self):
        return self.__seats_avail
    def get_details(self):
        return f"Train name is {self.train_name},Number is {self.train_no},total seats available is {self.__seats_avail}"
    #CLASS METHOD
    @classmethod                         
    def service(cls):
        return cls.services
class EVTrain(Train):
    def __init__(self, train_name, train_no, seats_avail):
        super().__init__(train_name, train_no, seats_avail)
    def get_details(self):
        return f"EV Train name is {self.train_name},Number is {self.train_no},total seats available is {self._Train__seats_avail}"
class Status:
    def __init__(self):
        self.Total_tickets=3000
        self.booked=[]
        self.cancelled=[]
class PassengerDetails(Status,EVTrain):
    def __init__(self,name,age,reservation_choice):
        super().__init__()
        self._name=name
        self.age=age
        self.reservation_choice=reservation_choice
    #INSTANCE METHODS
    def book_tickets(self,ticket_bought):
        self.booked.append(ticket_bought)
        self.Total_tickets-=1
        return f'Booked tickets are {self.booked}\nTotal Tickets Available are: {self.Total_tickets}'
    def cancel_ticket(self,ticket_to_cancel):
        if ticket_to_cancel in self.booked:
            self.cancelled.append(ticket_to_cancel)
            self.Total_tickets+=1
            return f'Cancelled ticekts are {self.cancelled}\nTotal Tickets Available are: {self.Total_tickets}'
    #STATIC METHOD
    @staticmethod
    def Ticket_Price(count,amt):                
        return len(count)*amt
c=EVTrain("hello",123,23)
print(c.get_details())
print(c.service())
p=PassengerDetails('gopi',23,'2s')
print(p.book_tickets('Hyd-Vij'))
print(p.book_tickets('Hy-Vij'))
print(p.cancel_ticket('Hyd-Vij'))
tot_amt=PassengerDetails.Ticket_Price(p.booked,167)-PassengerDetails.Ticket_Price(p.cancelled,167)
print(tot_amt)
