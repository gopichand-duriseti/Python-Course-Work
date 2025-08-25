#Q1)
class Students:
    total_students = 0   # Class variable shared by all objects

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.total_students += 1   # Increment whenever a new object is created
    @classmethod
    def get_total_students(cls):
        print(f"Total Students: {cls.total_students}")
    def display(self):
        return f'Name:{self.name},Age:{self.age}'
    @staticmethod
    def is_eligible(age):
        if 18<age<30:
            return True
        else:
            return False
# Creating students
s1 = Students("Arun", 20)
s2 = Students("Kiran", 22)
s3 = Students("Mohan", 19)
print(s1.display())
print(Students.is_eligible(25))
# Check total students
Students.get_total_students()

#Q2)
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_info(self):
        return f'Title:{self.title}\nAuthor:{self.author}\nPrice:${self.price}'
b=Book('The Alvhenist','Paulo Coelho',299)
print(b.display_info())

#Q3)
class Account:
    def __init__(self,account_holder,pin,balance=0):
        self.account_holder=account_holder
        self.__pin=pin
        self._balance=balance
    def deposit(self,amt):
        self._balance+=amt
        return f'Deposited:${amt}'
    def withdraw(self,pin,amt):
        if self.__pin==pin:
            self._balance-=amt
            return f'Withdrawn:${amt}'
    def show_balance(self):
        return self._balance
acc=Account('Ravi',1234)
print(acc.deposit(5000))
print(acc.withdraw(1234,1500))
print(acc.show_balance())

#Q4)
class User:
    def login(self):
        return 'User logged in'
class Rider(User):
    def book_ride(self):
        return 'Ride booked succesfully'
class Payment(Rider):
    def make_payment(self):
        return 'Payment Completed'
p=Payment()
print(p.login())
print(p.book_ride())
print(p.make_payment())

#Q5)
class LocationService:
    def track_location(self):
        return 'Current location tracked'
class OrderService:
    def place_order(self):
        return 'Order placed successfully'
class DeliveryApp(LocationService,OrderService):
    def confirm_delivery(self):
        return 'Delivery Confirmed to your address'
app=DeliveryApp()
print(app.track_location())
print(app.place_order())
print(app.confirm_delivery())

#Q8)
import math
class Shape:
    def __init__(self,val):
        self.val=val
    def area(self):
        pass
class Square(Shape):
    def area(self):
        return self.val*self.val

class Circle(Shape):
    def area(self):
        return math.pi*self.val*self.val
s=Square(4)
c=Circle(3)
print(s.area())
print(c.area())
        
#Q9)
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def display(self):
        return f'Sum:({self.x},{self.y})'
p1=Point(1,2)
p2=Point(3,4)
p3=p1 + p2
print(p3.display())

#Q10)
from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self):
        return f'Email sent to user@example.com'
class SMSNotification(Notification):
    def send(self):
        return f'SMS sent to registered number'
e=EmailNotification()
s=SMSNotification()
print(e.send())
print(s.send())