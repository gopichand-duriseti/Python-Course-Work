'''class shopping:
    products=[]
    discount=10 #The attribute that is defined inside class is called class attribute

    @classmethod
    def update(cls,new_discount):
        cls.discount=new_discount
        print(f'{new_discount} is updated')
    @classmethod
    def prod(cls):
        return cls.products
    def __init__(self,name):
        self.name=name
        print(self.name)
class shops(shopping):
    @classmethod
    def shopsclass(cls):
        return super().prod()
    def __init__(self,name):
        super().__init__(name)

s=shopping("gopi")
c=shops("gopal")
print(c.shopsclass())'''


'''Reversing the text
learn everything'''

f=open("example.txt",mode='r')
s=f.readlines()
l=0
for i in s:
    i=i.strip("\n").split()
    l+=len(i)
print(l)

import re
s="The following are emails:test@abc.com,hello123@gmail.com,user.name@gmail.com"
p=r'[A-Za-z0-9.]+@[a-z]+\.[a-z]{2,3}$'
f=re.findall(p,s)
print(f)

import re
s = "The following are emails:test@abc.com,hello123@gmail.com,user.name@gmail.com"
p = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}'
print(re.findall(p, s))

n='9392375981'
pat=r'^[6-9]\d{9}$'
print(re.fullmatch(pat,n))

#import numpy as np
'''t=np.random.randint(1,100,(1,10))
print(t.mean())
print(np.mean(t))
print(np.median(t))
print(t.std())
print(np.std(t))'''

'''A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(np.dot(A,B))'''