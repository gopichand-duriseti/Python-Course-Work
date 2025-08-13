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
from abc import ABC,abstractmethod

class TrainAb(ABC):
    @abstractmethod
    def get_details(self):
        pass
class Train(TrainAb):
    services=['Train Booking','Cancelling Train Ticket']
    def __init__(self,train_name,train_no,seats_avail,Tot_Train_Avail):
        self.train_name=train_name
        self.train_no=train_no
        self.__seats_avail=seats_avail
        self.Tot_Train_Avail=Tot_Train_Avail
    @property
    def seats_avail(self):
        return self.__seats_avail
    @seats_avail.setter
    def seats_avail(self,value):
        if value>=0:
            self.__seats_avail=value
        else:
            raise ValueError("Seats cannot be negative")
    def get_details(self):
        return f"Train name is {self.train_name},Number is {self.train_no},Total seats available is {self.seats_avail}"
    #CLASS METHOD
    @classmethod                         
    def service(cls):
        return cls.services
class EVTrain(Train):
    def get_details(self):
        return f"EV Train name is {self.train_name},Number is {self.train_no},Total seats available is {self.seats_avail}"
class Status:
    def __init__(self):
        self.booked=[]
        self.cancelled=[]
        self.passengers_name=set()
class PassengerDetails(Status,Train):
    def __init__(self,name,age,reservation_choice,train_name,train_no,seats_avail,Tot_Train_Avail):
        Status.__init__(self)
        Train.__init__(self,train_name,train_no,seats_avail,Tot_Train_Avail)
        self._name=name
        self.age=age
        self.reservation_choice=reservation_choice
    #INSTANCE METHODS
    def book_tickets(self,ticket_bought):
        self.booked.append(ticket_bought)
        self.seats_avail-=1
        self.passengers_name.add(self._name)
        return f'Booked tickets are {self.booked}\nTotal Seats Available are: {self.seats_avail}'
    def cancel_ticket(self,ticket_to_cancel):
        if ticket_to_cancel in self.booked:
            self.cancelled.append(ticket_to_cancel)
            self.seats_avail+=1
            return f'Cancelled ticekts are {self.cancelled}\nTotal Seats Available are: {self.seats_avail}'
    #STATIC METHOD
    @staticmethod
    def Ticket_Price(count,amt):                
        return len(count)*amt
    @staticmethod
    def passenger_count(count_pas):
        return len(count_pas)

t=Train("hii",134567,167,900)
print(t.get_details())
c=EVTrain("hello",123456,23,1000)
print(c.get_details())
print(c.service())
p=PassengerDetails('gopi',23,'2s','hello',12345678,160,1100)
print(p.book_tickets('Hyd-Vij'))
print(p.book_tickets('Hy-Vij'))
print(p.cancel_ticket('Hyd-Vij'))
print(PassengerDetails.passenger_count(p.passengers_name))
tot_amt=PassengerDetails.Ticket_Price(p.booked,167)
tot_amt_canc=PassengerDetails.Ticket_Price(p.cancelled,167)