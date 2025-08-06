print("ENCAPSULATION".center(100,'-'))

#PUBLIC,PROTECTED AND PRIVATE VARIABLES

class Details:
    def __init__(self,name,mail,pwd): #self is used to know which object it is pointing to
        self.name=name
        self._mail=mail
        self.__pwd=pwd
    def getpassword(self):
        return self.__pwd
    def setpassword(self,newpwd):
        self.__pwd=newpwd
        return self.__pwd
mukesh=Details("Mukesh Babu","mukesh@gmail.com","mukesh@68")
print(mukesh.name)
print(mukesh._mail) #If mukesh.mail:-#AttributeError: 'Details' object has no attribute 'mail'[PROTECTED VARIABLE]
print(mukesh.__pwd) #You can't access even after giving __pwd #AttributeError: 'Details' object has no attribute '__pwd'[PRIVATE VARIABLE]

#ONLY INSIDE YOU CAN ACCESS PWD
print(mukesh.getpassword())
print(mukesh.setpassword("MukeshBabu@70"))