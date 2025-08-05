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
        return self.price,self.name #price,name are called instance attributes(vary from one to another)
user1=shopping()
user2=shopping()
print(user1.product(3400,'laptop'))
print(shopping.discount) #10
print(user1.price) #3400