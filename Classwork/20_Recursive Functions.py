#sum
'''def sumofnum(n):
    if n==0:
        return 0
    return n+sumofnum(n-1)

n=int(input("Enter the value: "))
print(sumofnum(n))'''

#factorial
'''def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

n=int(input("Enter the value: "))
print(factorial(n))'''


#shoot
'''def shoot(n):
    if n==1:
        return 1
    print("Before Recursion:",n)
    shoot(n-1)
    print("After Recursion:",n)
    
n=int(input("Enter the value: "))
print(shoot(n))'''


#Sum of digits
#using while
'''n=int(input("Enter the number: "))
sum=0
while n>0:
    sum=sum+(n%10)
    n=n//10

print(sum)'''  


#using for loop
'''n=input("Enter the number: ")
sum=0
for i in n:
    sum+=int(i)
print(sum)'''

#using recursion
'''n=int(input("Enter the value: "))
def sumofdigits(n):
    if n == 0:
        return 0
    return n%10+sumofdigits(n//10)
print(sumofdigits(n))'''


#fibonacci series
'''n=int(input("Enter the number: "))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(b)
elif n>2:
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c'''



n=int(input("Enter the number: "))
a=0
b=1
if n==1:
    print(a)
elif n>=2:
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c
