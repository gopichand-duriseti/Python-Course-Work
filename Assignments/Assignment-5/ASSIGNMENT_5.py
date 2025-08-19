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
    def __init__(self,train_name,train_no,seats_avail,journeys=None):
        self.train_name=train_name
        self.train_no=train_no
        self.__seats_avail=seats_avail
        self.journey=journeys
    @property
    def seats_avail(self):
        return self.__seats_avail
    @seats_avail.setter
    def seats_avail(self,value):
        if value>=0:
            self.__seats_avail=value
        else:
            raise ValueError("Seats cannot be negative")
    def get_details(self): #get details of booked train
        return f"Train name is {self.train_name},train number is {self.train_no},Total seats available is {self.seats_avail} and journeys are '{self.journey}'"
    #CLASS METHOD
    @classmethod                         
    def service(cls):
        return cls.services
class ECTrain(Train):
    def get_details(self):
        return f"EC Train name is {self.train_name},train number is {self.train_no},Total seats available is {self.seats_avail} and journeys are '{self.journey}'"
class Status:
    def __init__(self):
        self.booked=[]
        self.cancelled=[]
        self.history={"booked":[],"cancelled":[]}
        self.passengers_name=set()
class PassengerDetails:
    def __init__(self, name=None, age=None, reservation_choice=None, train=None):
        self._name = name
        self.age = age
        self.reservation_choice = reservation_choice
        self.train = train
        self.status = Status()

    def book_tickets(self,ticket_bought):
        self.status.booked.append(ticket_bought)
        self.train.seats_avail-=1
        self.status.passengers_name.add(self._name)
        self.status.history['booked'].append(ticket_bought)
        print(self.status.history)
        return f'Booked tickets: {self.status.booked}, Seats left: {self.train.seats_avail}'
    
    def __str__(self):
        return f"Passenger: {self._name}, Age: {self.age}, Train: {self.train.train_name}, Seats left: {self.train.seats_avail}"


    def cancel_ticket(self,ticket_to_cancel):
        if ticket_to_cancel in self.status.booked:
            self.status.cancelled.append(ticket_to_cancel)
            self.train.seats_avail+=1
            self.status.history['cancelled'].append(ticket_to_cancel)
            print(self.status.history)
            return f'Cancelled ticekts are {self.status.cancelled},Total Seats Available: {self.train.seats_avail}'
    #STATIC METHOD
    @staticmethod
    def Tot_Ticket_Price_Booked(count,amt):                
        return len(count)*amt
    @staticmethod
    def passenger_count(count_pas):
        return len(count_pas)