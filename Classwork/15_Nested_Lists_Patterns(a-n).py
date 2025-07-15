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

Eg=int(input("Enter num: "))
for row in range(Eg):
    for col in range(Eg):
        if row==0 or col==0 or row==Eg-1 or col==Eg-1 or row ==Eg//2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

a=int(input("Enter rows for A pattern: "))
for row in range(a):
    for col in range(a):
        if row==0 or row==a//2 or col==0 or col==a-1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
b=int(input("Enter rows for B pattern: "))
for row in range(b):
    for col in range(b):
        if row==0 or row==b//2 or row==b-1 or col==0 or col==b-1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
c=int(input("Enter rows for C pattern: "))
for row in range(c):
    for col in range(c):
        if row==0 or row==c-1 or col==0:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
d=int(input("Enter rows for D pattern: "))
for row in range(d):
    for col in range(d):
        if (row==0 and col!=d-1) or (row==d-1 and col!=d-1) or col==0 or (col==d-1 and row not in (0,d-1)):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
e=int(input("Enter rows for E pattern: "))
for row in range(e):
    for col in range(e):
        if row==0 or row==e-1 or row==e//2 or col==0:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
f=int(input("Enter rows for F pattern: "))
for row in range(f):
    for col in range(f):
        if col==0 or row==0 or row==f//2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print() 
g=int(input("Enter rows for G pattern: "))
for row in range(g):
    for col in range(g):
        if row==0 or col==0 or (col in range(g//2,g) and row == g//2) or (row==g-1 and col not in range(g//2+1,g-1)) or (row in range(g//2+1,g-1) and col in (g//2,g-1)):
        #row==0 or col==0 or (col in range(1,g//2) and (row==0 or row==g-1)) or (col==(g//2) and row in range(g//2,g)) or (row ==g//2 and col in range(g//2+1,g)) or (row not in range(0,g//2+1) and col==g-1):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print() 
o_g=int(input("Enter rows for other G pattern: "))
for row in range(o_g):
    for col in range(o_g):
        if row==0 or col==0 or row==o_g-1 or (col in range(o_g//2,o_g) and row == o_g//2) or (row in range(o_g//2+1,o_g-1) and col==o_g-1):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print() 
h=int(input("Enter rows for H pattern: "))
for row in range(g):
    for col in range(g):
        if col==0 or col==h-1 or row==h//2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
i=int(input("Enter rows for I pattern: "))
for row in range(i):
    for col in range(i):
        if row==0 or row==i-1 or col==i//2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
j=int(input("Enter rows for J pattern: "))
for row in range(j):
    for col in range(j):
        if row==0 or col==j//2 or (row in range(j//2+1,j-1) and col ==0) or (row==j-1 and col in range(0,j//2)):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
k=int(input("Enter rows for K pattern: "))
for row in range(k):
    for col in range(k):
        if col==0  or (row+col==k-1 and col not in range(1,k//2)) or (col in range(1,k//2) and row == k//2) or (row==col and row>k//2):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
l=int(input("Enter rows for L pattern: "))
for row in range(l):
    for col in range(l):
        if col==0 or row==l-1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
m=int(input("Enter rows for M pattern: "))
for row in range(m):
    for col in range(m):
        if col==0 or col==m-1 or (row in range(1,m//2+1) and row==col) or (row==col==m//2) or (row+col==k-1 and row < k//2):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
n=int(input("Enter rows for N pattern: "))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==col:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()

    