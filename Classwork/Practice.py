'''v=int(input("Enter rows for V pattern: "))
for row in range(v):
    for col in range(v):
        if (col in (0,v-1) and row in range(0,v//2+1)) or (row==v-1 and col==v//2) or ((row-col==v//2 or (row+col)/3==v//2) and row in range(v//2+1,v-1)):
        #row==a//2 or (col==a//2 and row==0) or (row+col==a-1 and row in range(1,a//2)) or (row==col and row in range(1,a//2)) or (col==0 and row in range(a//2+1,a)) or (col==a-1 and row in range(a//2+1,a)):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
'''
#RECCURSION,LAMBDA,MODULE,GENERATORS
import math,random
'''
l=['Alice','Bob','Charlie','David']
print(random.choices(l,k=2))

l=[36,42,39,45,41]
s=list(filter(lambda x:x>40,l))
print(s)

def is_prime(n,i=2):
    if n%i==0:
        print("Not a prime")
        return 
    else:
        if i<n:
            return is_prime(n,i+1)
        print("Prime number")
is_prime(15)

#OPTIMIZED PRIME NUMBER RECCURSION
def is_prime(n, i=2):
    if n <= 1:
        print("Not a prime")
        return
    if i * i > n:   # ✅ base condition (stop recursion)
        print("Prime number")
        return
    if n % i == 0:
        print("Not a prime")
        return
    return is_prime(n, i + 1)

is_prime(21)
  
def r(n):
    if n==0:
        return ''
    else:
        return int(str(n%10)+str(r(n//10)))
print(r(1234))

s=['apple','Apple','Banana','BANANA','Cherry']
l=set(map(lambda x:x.lower(),s))
print(sorted(list(l)))

def c(n):
    for i in range(n,-1,-1):
        yield i
d=c(3)
print(next(d))
print(next(d))
print(next(d))
print(next(d))

s = [[1,2],[3,[4,5]]]

def add(lst):
    total = 0
    for i in lst:
        if isinstance(i, list):
            total += add(i)
        else:
            total += i
    return total

print(add(s))  # 15

s = [[1,2],[3,[4,5]],[[5,6],[6,7]]]
total = 0

for i in s:
    if isinstance(i, list):
        for j in i:
            if isinstance(j, list):   # check again for deeper nesting
                for k in j:
                    total += k
            else:
                total += j
    else:
        total += i

print(total)  # 15
'''

#FUNCTIONS
'''
def c(w,h):
    return w/(h*h)
print(round(c(70,1.75),2))

def f(l):
    x=list(filter(lambda x:x%2==0,l))
    return x
print(f([1,2,3,4,5,6,7,8]))

n=2
s=[n*i for i in range(1,11)]
print(s)

from collections import Counter
s="this is a test this is"
d={}
for i in s.split():
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

print(dict(Counter(s.split())))

n=12
for i in range(1,n+1):
    if n%i==0:
        print(i)


nested = [[1,2],[3,[4,5]],[[5,6],[6,7],[8,9,[10,11]]]]

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))  # go deeper
        else:
            result.append(i)
    return result

print(flatten(nested))

s='17-07-2025'
s=s.split('-')
print('/'.join(s[::-1]))

v='hello world'
for i in v:
    if i in 'aeiou':
        v=v.replace(i,'*')
print(v)

l='python'
vow='aeiou'
vol=list(map(lambda i:'*' if i in vow else i,l)) #map is going to update the element
print(vol)

s='hello world'
l=' '.join([i[::-1] for i in s.split()])
print(l)

l=map(int,input().split())
x=list(filter(lambda x:x!=0,l))
print(x)
'''

a,b,c=1.345,2,3
print("a:",a,"b:",b) #a: 1 b: 2

print(f'a:{a:.1f}\nb:{b}')