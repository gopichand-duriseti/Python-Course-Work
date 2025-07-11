t=(1,2,3,4,'strings')
t1=(5,6,7,'lists')
print(t+t1)
print(t[0:4]*3)
'''TUPLE PACKING AND UNPACKING'''
t=(1,2,3)
a,b,c=t #Means a value is 1,b is 2,c is 3)
'''a,b=t #Value Error:Too Many Values'''
numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers #a is 1,b is 2,rest is [3,4,5]
res=('gopi','gd1234@gmail.com','Employee')
name,mail,role=res
t=(1,2,3,4,5,[1,2])
t[5].append(3)
print(t) #(1,2,3,4,5,[1,2,3])
d=[('name','gopi'),('mail','gd1234@gmail.com')]
print(dict(d)) #{'name': 'gopi', 'mail': 'gd1234@gmail.com'}

