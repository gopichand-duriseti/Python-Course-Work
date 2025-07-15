#NESTED LOOPS means loop within the loop

#OUTER LOOP means 'rows' and INNER LOOP means 'columns'

for row in range(5):
    for column in range(5):
        print(f"*",end=" ")
    print()

for row in range(5):
    for column in range(5):
        print(row,end=" ")
    print()

for row in range(5):
    for column in range(5):
        print(column,end=" ")
    print()

for row in range(5):                #for row in range(1,6)
    for column in range(row+1):     #for column in range(row)
        print("*",end=" ")
    print()

for row in range(5):                #for row in range(5,0,-1)      #for row in range(5)
    for column in range(5,row,-1):  #for column in range(row,0,-1) #for column in range(5-row)
        print("*",end=" ")
    print()

for row in range(5):
    for j in range(5-row-1):
        print(" ",end=" ")
    for k in range(row+1):
        print("*",end=" ")
    print()

for row in range(5):
    for j in range(row):
        print(" ",end=" ")
    for k in range(5-row):
        print("*",end=" ")
    print()

n=int(input("Enter n: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

a=int(input("Enter a: "))
for row in range(a):
    for col in range(a):
        if row==0 or col==0 or row==a-1 or col==a-1 or row ==a//2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

z=int(input("Enter rows for Z pattern: "))
for row in range(z):
    for col in range(z):
        if row==0 or row==z-1 or row+col==z-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

x=int(input("Enter rows for X pattern: "))
for row in range(x):
    for col in range(x):
        if row+col==x-1 or row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

a=int(input("Enter rows for A pattern: "))