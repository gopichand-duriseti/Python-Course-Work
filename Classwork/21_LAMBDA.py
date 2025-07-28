'''A lambda function is a small anonymous function that is used to perform short tasks
without defining a full function using def.'''
n=int(input())
squ=lambda n:n*n
print(squ(n))

a=int(input())
b=int(input())
divl=lambda a,b:a/b
print(f'{divl(a,b):.2f}')

l=[1,2,3,4,5]
squa=list(map(lambda i:i**2,l))
print(squa)

l=['gopi chand','mukesh','rahul']
lam=list(map(lambda i:i.title(),l))
print(lam)

l='python'
vow='aeiou'
vol=list(map(lambda i:'*' if i in vow else i,l)) #map is going to update the element
print(vol)
'''---------------------------------------------------------------------------------------------'''
l=[1,2,3,4,5,6,7,8,9]
evenf=list(filter(lambda x:x%2==0,l))
print(evenf)

l=[1,0,0,0,2,0,3,5,0,6,7]
notzero=list(filter(lambda x:x!=0,l))
print(notzero)

data={'gopi':False,'Mukesh':True,'Rahul':True}
d=list(filter(lambda i:data[i],data)) 
print(d) #{'Mukesh','Rahul'}
'''---------------------------------------------------------------------------------------------'''
from functools import reduce

numbers=[1,2,3,4]
red_add=reduce(lambda x,y:x+y,numbers)
print(red_add) #10
'''---------------------------------------------------------------------------------------------'''
data={'Mukesh':98,'Rahul':99,'gopi':97}
dic=dict(sorted(data.items(),key=lambda x:x[1])) #dict(sorted(data.items(),key=lambda x:x[1],reverse=True))-ascending order
print(dic)