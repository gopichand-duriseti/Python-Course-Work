import sys 
import platform
import math
import random
import collections

print(sys.argv)

print(platform.system())
print(platform.version())
print(platform.processor())

print(math.sqrt(5))
print(math.pow(3,2))
print(math.fabs(23-29))
print(math.floor(23.4)) #highest integer/decimal less than the given value -23
print(math.ceil(24.1)) #lowest integer value greater than given value -25

print(random.randint(1,10))
print(random.choice([1,2,3,4,5])) #3 5
print(random.choices([1,2,3,4,5])) #[3] [5]
print(random.choices([1,2,3,4,5,6],k=3)) 
print(random.random()) #random in 0 to 1
print(random.sample(['Gopi','Mukesh'],counts=[4,2],k=5)) #k is the limit
print(random.uniform(2,7))
l=['Mukesh','Gopal','Rahul','Sanjay']
#random.seed() #seed helps us to print same values continuously
print(l) 

