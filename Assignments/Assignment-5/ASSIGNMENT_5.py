#TRAIN
#service=online #class variable
#ECTRAIN(TRAIN) #Inheritance
#name,age,seats_available(attributes)---_name(protected),__seats_available(private),age(public) #encapsulation
#Book_Ticket and Cancel_Ticket(Methods)---Instance method
#display_details(self)---related to train
#display_details(self)---related to ectrain #polymorphism
#@classmethod #def servicing(cls):return cls.service---class method
#@staticmethod #if __seats_available>0

# Printing the IRCTC banner
print("IRCTC".center(100, "-"))

# Importing Abstract Base Class (ABC) and abstractmethod for abstraction
from abc import ABC, abstractmethod


# ----------------------------
# ABSTRACT CLASS
# ----------------------------
class TrainAb(ABC):
    """Abstract class for trains"""

    @abstractmethod
    def get_details(self):
        """Abstract method that must be implemented in child classes"""
        pass


# ----------------------------
# TRAIN CLASS (Normal Trains)
# ----------------------------
class Train(TrainAb):
    # Class variable (shared across all Train objects)
    services = ['Train Booking', 'Cancelling Train Ticket']

    def __init__(self, train_name, train_no, seats_avail, journeys=None):
        # Public attributes
        self.train_name = train_name
        self.train_no = train_no
        self.journey = journeys
        # Private attribute (encapsulation)
        self.__seats_avail = seats_avail

    # Getter for private attribute
    @property
    def seats_avail(self):
        return self.__seats_avail

    # Setter with validation
    @seats_avail.setter
    def seats_avail(self, value):
        if value >= 0:
            self.__seats_avail = value
        else:
            raise ValueError("Seats cannot be negative")

    # Method to show train details
    def get_details(self):
        return f"Train name is {self.train_name}, train number is {self.train_no}, " \
               f"Total seats available is {self.seats_avail} and journeys are '{self.journey}'"

    # Class method (belongs to class not instance)
    @classmethod
    def service(cls):
        return cls.services


# ----------------------------
# EC TRAIN CLASS (Special Trains)
# ----------------------------
class ECTrain(Train):
    """Inherits Train but overrides get_details"""

    def get_details(self):
        return f"EC Train name is {self.train_name}, train number is {self.train_no}, " \
               f"Total seats available is {self.seats_avail} and journeys are '{self.journey}'"


# ----------------------------
# STATUS CLASS (Track Bookings/History)
# ----------------------------
class Status:
    def __init__(self):
        # Lists to store bookings and cancellations
        self.booked = []
        self.cancelled = []
        # Dictionary to maintain full history
        self.history = {"booked": [], "cancelled": []}
        # Set for unique passenger names
        self.passengers_name = set()


# ----------------------------
# PASSENGER CLASS
# ----------------------------
class PassengerDetails:
    # Class-level list to keep track of ticket prices
    u=0
    def __init__(self, name=None, age=None, reservation_choice=None, train=None, status=None):
        self._name = name
        self.age = age
        self.reservation_choice = reservation_choice
        self.train = train
        self.status = status  # Shared status object

    # Book tickets
    def book_tickets(self, ticket_bought):
        if self.train.seats_avail > 0:
            self.status.booked.append(ticket_bought)                # add to booked list
            self.train.seats_avail -= 1                             # decrease seat count
            self.status.passengers_name.add(self._name)             # add passenger name
            self.status.history['booked'].append(ticket_bought)     # update history
            return f'Booked tickets: {self.status.booked}'
        else:
            return "No seats left for this Train"

    # String representation of passenger object
    def __str__(self):
        return f"Passenger: {self._name}, Age: {self.age}, Train: {self.train.train_name}, Seats left: {self.train.seats_avail}"

    # Cancel tickets
    def cancel_ticket(self, ticket_to_cancel):
        if ticket_to_cancel in self.status.booked:
            self.status.booked.remove(ticket_to_cancel)
            self.status.cancelled.append(ticket_to_cancel)              # add to cancelled
            self.train.seats_avail += 1                                 # increase seat count
            self.status.history['booked'].remove(ticket_to_cancel)         
            self.status.history['cancelled'].append(ticket_to_cancel)   # update history
            return f'Cancelled tickets are {self.status.cancelled}'

    # Show full booking/cancellation history
    def train_history(self):
        return self.status.history

    # Class method → returns ticket list
    @classmethod
    def ticket(cls):
        return cls.u

    # ----------------------------
    # STATIC METHODS
    # ----------------------------

    # Calculate total ticket price
    @staticmethod
    def Tot_Ticket_Price_Booked(s, amt):
        s+=amt
        return s
    @staticmethod
    def Tot_Ticket_Price_Cancelled(s,amt):
        s-=amt
        return s


    # Count total passengers
    @staticmethod
    def passenger_count(count_pas):
        return count_pas
    
    @staticmethod
    def difference(s):
        return s
