#METHOD OVERRIDING(same method,same parameters,different behavior)
class normalUser:
    def playvideo(self,name):#class normalUser: #base/parent class
        print(f"{name} is playing video with: \n1.Normal Quality\n2.Ads Run\n3.No Backgound Playing\n4.Limited Videos download\n5.Music with ads\n")
    def likes(self):
        pass
    def comments(self):
        pass
    def share(self):
        pass
    def title(self):
        pass
    def description(self):
        pass
    def subscribe(self):
        pass

class premiumUser(normalUser):
    def playvideo(self,name):
        print(f"{name} is playing video with: \n1.High Quality\n2.No Ads\n3.Backgound Playing\n4.Download anything\n5.Music without ads\n")
def play_video(user,username):
    user.playvideo(username)
gopi=normalUser()
gopal=premiumUser()
mohit=normalUser()
tarak=premiumUser()
sanjay=premiumUser()
arun=normalUser()

gopi.playvideo('gopi')
gopal.playvideo('gopal')
        #OR
play_video(gopi,"gopi")
play_video(gopal,"gopal")
play_video(mohit,"mohit")
play_video(tarak,"tarak")
play_video(sanjay,"sanjay")
play_video(arun,"arun")

#OPERATOR OVERLOADING 
#TO USE +,-,.... operators we have to overload it
class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __str__(self):
        return f"{self.n}"
'''
__sub__(self,other)
__mul__(sef,other))
__lt__(self,other)
__gt__(self,other)
__eq__(self,other)
'''
number1=number(10)
number2=number(20)
'''print(number1) #<__main__.number object at 0x000002586A5B6CF0>
after using __str__ constructor you can get the value'''
print(number1) #10 
#number3=number(30)
#print(number1+number2) #before adding add constructor #adding two variables #Typeerror:unsupported operand type(s) for +: 'number' and 'number'
print(number1+number2) #30