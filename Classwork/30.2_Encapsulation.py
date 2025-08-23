print("ENCAPSULATION".center(100,'-'))

#PUBLIC,PROTECTED AND PRIVATE VARIABLES

class Details:
    def __init__(self,name,mail,pwd): #self is used to know which object it is pointing to
        self.name=name
        self._mail=mail
        self.__pwd=pwd
    def getpassword(self): #getter method
        return self.__pwd
    def setpassword(self,newpwd):#setter method
        self.__pwd=newpwd
        return self.__pwd
mukesh=Details("Mukesh Babu","mukesh@gmail.com","mukesh@68")
print(mukesh.name)  #PUBLIC VARIABLE
print(mukesh._mail) #If mukesh.mail:-#AttributeError: 'Details' object has no attribute 'mail'[PROTECTED VARIABLE]
'''print(mukesh.__pwd) #You can't access even after giving __pwd #AttributeError: 'Details' object has no attribute '__pwd'[PRIVATE VARIABLE]
'''
#ONLY INSIDE YOU CAN ACCESS PWD
print(mukesh.getpassword())
print(mukesh.setpassword("MukeshBabu@70"))

class Bank:
    def __init__(self):
        self.name='xyz'
        self.__balance=0
    @property
    def noresbalance(self):
        return self.__balance
    @noresbalance.setter
    def noresbalance(self,amount):
        self.__balance+=amount

b=Bank()
print(b.noresbalance) #0
b.noresbalance=3000
print(b.noresbalance) #3000
b.noresbalance=5000
print(b.noresbalance) #8000

print(b.name)
b.name='abc'
print(b.name)


