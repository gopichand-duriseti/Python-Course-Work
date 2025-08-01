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

n='1243f2f34r'
print(dict(collections.Counter(n)))
d=collections.defaultdict(int)
for i in n:
    d[i]+=1 #d['1']+=1 :- {'1':1} Normally it gives error if not used defaultdict
print(d) #no need of using if else to form the key:value pairs if using defaultdict

from itertools import combinations,permutations
from collections import deque

l=[3,4,5,1,2]
res=list(combinations([1,2,3,4,5],3))
print(res)
for i in range(len(l)-1):
    for j in range(i+1,len(l)): 
        print(l[i],l[j]) #0,1 #0,2 #0,3 #0,4 #1,2 #1,3 #1,4 #2,3 #2,4 #3,4

'''
#SNAKE AND LADDER
Sanjay_score=0
Sumanth_score=0
snakes={3:0,99:54,77:49,21:12,96:5,50:20,7:5,19:9,32:12,46:6,68:39,80:40}
ladders={2:17,13:63,10:98,24:76,33:56,79:84,88:92}

while Sanjay_score<50 and Sumanth_score<50:
    san=input("Sanjay-[s]top or [c]ontinue: ")
    if san=='c':
        san_turn=random.randint(1,6)
        Sanjay_score+=san_turn
        if Sanjay_score in snakes:
            Sanjay_score=snakes[Sanjay_score]
            print(f"\n-------Sanjay-Snake bite-Sanjay_score: {Sanjay_score}-Dice:{san_turn}\n")
        elif Sanjay_score in ladders:
            Sanjay_scores=ladders[Sanjay_score]
            print(f"\n*******Sanjay-Ladder-Sanjay_score: {Sanjay_score}-Dice:{san_turn}\n")
        else:
            print(f"\nSanjay_score: {Sanjay_score}-Dice:{san_turn}\n")
    else:
        print('Sumanth Wins')
        break
    sam=input("Sumanth-[s]top or [c]ontinue: ")
    if sam=='c':
        sum_turn=random.randint(1,6)
        Sumanth_score+=sum_turn
        if Sumanth_score in snakes:
            Sumanth_score=snakes[Sumanth_score]
            print(f"\n-------Sumanth-Snake bite-Sumanth_score: {Sumanth_score}-Dice:{sum_turn}\n")
        elif Sumanth_score in ladders:
            Sumanth_score=ladders[Sumanth_score]
            print(f"\n*******Sumanth-Ladder-Sumanth_score: {Sumanth_score}-Dice:{sum_turn}\n")
        else:
            print(f"\nSumanth_score: {Sumanth_score}-Dice:{sum_turn}\n")
    else:
        print(f'Sanjay Wins')
        break
if Sanjay_score>Sumanth_score:
    print(f'Sanjay Wins')
elif Sanjay_score<Sumanth_score:
    print('Sumanth Wins')
else:
    print("It's a tie")
    '''
