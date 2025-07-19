#There are 4 types of arguments:
'''
1)POSITIONAL ARGUMENTS:-Arguments are passed in the order they are defined in the function.(Based on position it is going to map)
2)KEYWORD ARGUMENTS:-Arguments are specified with the parameter names.
3)DEFAULT ARGUMENTS:-Provides default values if no argument is provided.
4)Variable-Length Arguments:-*args (Arbitrary Positional Arguments):Used to pass a variable number of arguments.
                             **kwargs (Arbitrary Keyword Arguments):Used to pass multiple keyword arguments.
'''
#POSITIONAL ARGUMENTS
def display(email,pwd,name): #Here pwd is name and name is pwd considering the parameters given in display() below
    print(email,name,pwd,sep=',') 
email,names,pwd='gopi@1111',['gopi','gopal'],'1234'
display(email,names,pwd) #1234 gopi
#KEYWORD ARGUMENTS
def display(email,pwd,name): 
    print(email,name,pwd) 
display(email='gopi@111',name='gopi',pwd='1234')
#DEFAULT ARGUMENTS
def display(email,pwd,name='gopi'): 
    print(email,name,pwd) 
display('gopi@1934',1234) #if name='gopiii' given here it'll overwrite/update name
#Variable-Length Arguments:#*args (Arbitrary Positional Arguments):
def display(*var):
    print(var)
display('gopi',1234,'gopi123','present') #('gopi', 1234, 'gopi123', 'present')
#**kwargs (Arbitrary Keyword Arguments):Used to pass multiple keyword arguments.
def display(**kwargs):
    print(kwargs)
display(name='gopi',pwd=1234,mail='gopi@123',status='present') #{'name': 'gopi', 'pwd': 1234, 'mail': 'gopi@123', 'status': 'present'}

#SCOPE OF VARIABLES
#GLOBAL SCOPE,LOCAL SCOPE,NON-LOCAL SCOPE,BUILT-IN SCOPE(Overwrite built-in functions if we take those as variable[eg:len=5])
batch=30                                #def wish(name):
def wish(name):                             #global batch
    print(name)
name=input("Enter name:")    #OR
wish(name)
print(batch)

def wish(name):
    print(name)
    def batch():
        nonlocal batch
        batch=30
    print(batch)
    batch()
name=input("Enter your name: ")
wish(name)   #gopi
             #<function wish.<locals>.batch at 0x0000025BB8E6C220>
print(batch) #30 

#FACTORIAL
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i 
        print(f'{i}!={fact}')
    print(fact)
factorial(int(input("Enter the number: ")))

#FIBONACCI SERIES
a,b=0,1
n=int(input("Enter n:"))
print(a,b,sep=' ',end=' ')
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
