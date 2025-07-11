#OPERATORS:
'''1)ARITHMETIC OPERATORS'''
a=10
b=20
print('***ARITHMETIC OPERATORS***')
print("Add(+):",a+b) #Add(+): 30
print("Sub(-):",a-b) #Sub(-): -10
print("Mul(*):",a*b) #Mul(*): 200
print("Div(/):",a/b) #Div(/): 0.5
print("Floor Div(//):",a//b)#Floor Div(//): 0
print("Modulus(%):",a%b) #Modulus(%): 10
print("Exp(**):",a**b)#Exp(**): 100000000000000000000

'''2)COMPARISION OPERATORS'''
#Note:a-z ASCII value(97-122) and A-Z ASCII value(65-90),Even if a and b are strings you can still use ">","<",...operators
c=10
d=40
print('***COMPARISION OPERATORS***')
print("Equal to(==):",c==d) #Equal to(==): False
print("Not Equal to(!=):",c!=d)#Not Equal to(!=): True
print("Greater Than(>):",c>d) #Greater Than(>): False
print("Less Than(<):",c<d) #Less Than(<): True
print("Greater Than or Equal to(>=):",c>=d) #Greater Than or Equal to(>=): False
print("Less Than or Equal to(<=):",c<=d) #Less Than or Equal to(<=): True

'''3)ASSIGNMENT OPERATORS'''
'''var =var(op)(val)
e=e+10
e+=10'''
e=20
print('***ASSIGNMENT OPERATORS***')
print("Add & Assign(e+=40):",e+40) #Add & Assign(e+=40): 60
print("Subtract & Assign(e-=10):",e-10) #Subtract & Assign(e-=10): 10
print("Multiply & Assign(e*=2):",e*2) #Multiply & Assign(e*=2): 40
print("Divide & Assign(e/=2):",e/2) #Divide & Assign(e/=2): 10.0
print("Floor Divide & Assign(e//=2):",e//2) #Floor Divide & Assign(e//=2): 10
print("Modulus & Assign(e%=3):",e%3) #Modulus & Assign(e%=3): 2
print("Exponentiate & Assign(e**=2):",e**2) #Exponentiate & Assign(e**=2): 400

'''4)LOGICAL OPERATORS'''
#To Watch post of some Instagram User
follower=True
public=False
canview=(follower ==True or public==True)
print('***LOGICAL OPERATORS***')
print(canview) #True

'''5)MEMBERSHIP OPERATORS'''
names=['Siddhartha','Gopal','Charan Sai','Revanth']
print('***MEMBERSHIP OPERATORS***')
print('in result:','Charan Sai'  in names) #in result: True
print('not in result:','gopi' not in names) #not in result: True

'''6)IDENTITY OPERATORS'''
l=[1,2,3,4]
b=[1,2,3,4]
#Identical means same memory allocation
print('***IDENTITY OPERATORS***')
l==b 
print("l is b:",l is b) #False
print("id(l)",id(l)) #id(l) 3088102787968
print("id(b)",id(b)) #id(b) 3088102788416
print("because id(l) and id(b) aren't same or not having same memory allocation")
a=b
print("a is b:",a is b) #True
print("id(a)",id(a)) #id(a) 3088102788416
print("id(b)",id(b)) #id(b) 3088102788416
print('because id(a) and id(b) are same')

'''6)BITWISE OPERATORS'''
print('***BITWISE OPERATORS***')
print('3&5:',3&5) #3&5: 1
print('4|5:',4|5) #4|5: 5
print('5^6:',5^6) #5^6: 3
print('Bitwise Not FORMULA:-(n+1),Eg:~1=-2,~8=-9')
print('~1:',~1) #~1: -2


