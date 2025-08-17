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
class PassengerDetails:
    def __init__(self,name,age,reservation_choice,train:Train):
        self._name=name
        self.age=age
        self.reservation_choice=reservation_choice
        self.train=train
        self.status=Status()

    def book_tickets(self,ticket_bought):
        self.status.booked.append(ticket_bought)
        self.train.seats_avail-=1
        self.status.passengers_name.add(self._name)
        return f'Booked tickets: {self.status.booked}, Seats left: {self.train.seats_avail}'

    def cancel_ticket(self,ticket_to_cancel):
        if ticket_to_cancel in self.status.booked:
            self.status.cancelled.append(ticket_to_cancel)
            self.train.seats_avail+=1
            return f'Cancelled ticekts are {self.status.cancelled},Total Seats Available: {self.train.seats_avail}'
    #STATIC METHOD
    @staticmethod
    def Tot_Ticket_Price_Booked(count,amt):                
        return len(count)*amt
    @staticmethod
    def passenger_count(count_pas):
        return len(count_pas)

#Cost should be checked by considering train and reservation choice
t=Train("hii",134567,190,900)
print(t.get_details())
c=EVTrain("hello",123456,23,1000)
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

