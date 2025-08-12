print("OBJECT ORIENTED PROGRAMMING LANGUAGE".center(100,'-'))
'''
class Insta2010:
    followers=set()
    addfollowers()
    removefollowers()
    following={}
    addfollowing()
    unfollow()
    username=''
    bio=''
    post=[]
    closefriends=[]
    highlights=[]
    block()
    unblock()
    blockpeople={}
    share()
    sendrequest()
    reels()
    sendmessage()

gopi=Insta()
gopi.share()

Sanjay=Insta()
Sanjay.bio='hii peoooopleeeeee'

'''

class number:
    a=10
    def update(self,number):
        self.b=number
        print(self.b)
n1=number()
n2=number()
n1.update(5)

class shopping:
    discount=10 #The attribute that is defined inside class is called class attribute
    def product(self,price,name):
        self.price=price
        self.name=name
        return self.price,self.name #price,name are called instance attributes(vary from user to user)
user1=shopping()
user2=shopping()
print(user1.product(3400,'laptop'))
print(shopping.discount) #10
print(user1.price) #3400
user1.price=4000
shopping.discount=13 

#METHODS - CLASS,INSTANCE AND STATIC METHOD

#Class Method
class shopping:
    discount=10 #The attribute that is defined inside class is called class attribute

    @classmethod
    def update(cls,new_discount):
        cls.discount=new_discount
        print(f'{new_discount} is updated')
    def product(self,price,name):
        self.price=price
        self.name=name
        return self.price,self.name
user1=shopping()
shopping.update(15)

#Static Method (used for calculations)
class shopping:
    products=[]
    discount=10 #The attribute that is defined inside class is called class attribute

    @classmethod
    def update(cls,new_discount):
        cls.discount=new_discount
        print(f'{new_discount} is updated')
    def product(self,price,name): #Even if you use anything in place of self we will get the output
        self.price=price
        self.name=name
        return self.price,self.name
    @staticmethod
    def check(products,price):
        if products:
            print(f"Go and shop,Items available:-{products}")
        else:
            print('Out of Stock')
            return False
        if price:
            print("price:","$%.2f"%price,sep='-')
        
user1=shopping()
user1.check([],0000)
shopping.check(['laptop','mobile'],4000) #can access products and price using both class name and object name

'''Write a python program to Create a class Department with the following: Attributes: dept_name (string) hod_name (string) faculty_count (integer) Method: is_faculty_sufficient(min_count) Returns "Yes" if faculty_count == min_count, otherwise "No" Input Format :First line: Department name (string) ,Second line: HOD name (string) ,Third line: Faculty count (integer) and Fourth line: Minimum required count (integer) Output Format :A single line: "Yes" if faculty is sufficient, else "No"'''
class Department:
    def __init__(self,dept_name,hod_name,fac_count):
        self.deptname=dept_name
        self.hodname=hod_name
        self.fac_count=fac_count
    @staticmethod
    def is_fac_suf(min_c):
        if min_c==fac_count:
            return "Yes"
        else:
            return "No"
dept_name=input()
hod_name=input()
fac_count=int(input())
min_c=int(input())
c=Department(dept_name,hod_name,fac_count)
print(c.is_fac_suf(min_c))

'''Write a python program to Create a class Department with the following: Attributes: dept_name (string) hod_name (string) faculty_count (integer) 
Method: is_faculty_sufficient(min_count) Returns "Yes" if faculty_count == min_count, otherwise "No" 
Input Format :First line: Department name (string) ,Second line: HOD name (string) ,Third line: Faculty count (integer) and Fourth line: Minimum required count (integer) 
Output Format :A single line: "Yes" if faculty is sufficient, else "No"'''
class Department:
    def __init__(self,dept_name,hod_name,fac_count):
        self.deptname=dept_name
        self.hodname=hod_name
        self.fac_count=fac_count
    @staticmethod
    def is_fac_suf(min_c):
        if min_c==fac_count:
            return "Yes"
        else:
            return "No"
dept_name=input()
hod_name=input()
fac_count=int(input())
min_c=int(input())
c=Department(dept_name,hod_name,fac_count)
print(c.is_fac_suf(min_c))