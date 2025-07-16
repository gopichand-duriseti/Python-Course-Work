o=int(input("Enter rows for O pattern: "))
for row in range(o):
    for col in range(o):
        if row==0 or row==o-1 or col in (0,o-1):
        #(row!=0 and row !=o-1 and col in (0,o-1)) or (row==0 and col!=0 and col!=o-1) or (row==o-1 and col!=0 and col!=o-1): #Perfect O
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
p=int(input("Enter rows for P pattern: "))
for row in range(p):
    for col in range(p):
        if col==0 or (col in range(1,p) and (row == 0 or row==p//2)) or (row in range(1,p//2) and col==o-1) :
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
q=int(input("Enter rows for Q pattern: "))
for row in range(q):
    for col in range(q):
        if (row in range(1,q//2+1) and col in (0,q-1)) or (row==0 and col not in (0,q-1)) or (row==q//2+1 and col not in (0,q-1)) or (row==col==q//2) or (row==col and row in range(round(q//2)+1,q) and col in range(round(q//2)+1,q)):
        #(row in range(1,q//2+1) and col in (0,q-1)) or (row==0 and col not in (0,q-1)) or (row==q//2+1 and col not in (0,q-1)) or (row==col==q//2+1) or (row+1==col and row in range((q//2),q+1) and col in range((q//2)+1,q+1)):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
r=int(input("Enter rows for R pattern: "))
for row in range(r):
    for col in range(r):
        if col==0 or row==0 or (row+col==r-1 and row in range(0,r//2)) or (row==col and row in range(r//2+1,r)) or (col in range(1,r//2+1) and row==r//2):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
s=int(input("Enter rows for S pattern: "))
for row in range(s):
    for col in range(s):
        if row==0 or row==s-1 or row==s//2 or (row in range(1,s//2) and col==0) or (row in range(s//2+1,s-1) and col==s-1):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
t=int(input("Enter rows for T pattern: "))
for row in range(t):
    for col in range(t):
        if row==0 or col==t//2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
u=int(input("Enter rows for U pattern: "))
for row in range(u):
    for col in range(u):
        if (col==0 and row!=u-1) or (col==u-1 and row!=u-1) or (col in range(1,u-1) and row==u-1):
        #row==u-1 or col==0 or col==u-1::
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()   
v = int(input("Enter rows for V pattern: "))
for row in range(v):
    for col in range(v * 2 - 1):  # to make symmetric V
        if col == row or col == (2 * v - 2 - row):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
w=int(input("Enter rows for W pattern: "))
for row in range(w):
    for col in range(w):
        if col==0 or col==w-1 or (row+col==w-1 and row > w//2) or (row==col and row > w//2) or (row==col==w//2):
        #row==u-1 or col==0 or col==u-1:
            print("*",end=' ')
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
y=int(input("Enter rows for Y pattern: "))
for row in range(y):
    for col in range(y):
        if (col==y//2 and row in range(y//2,y)) or (row+col==y-1 and row in range(0,y//2)) or (row==col and row in range(0,y//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

z=int(input("Enter rows for Z pattern: "))
for row in range(z):
    for col in range(z):
        if row==0 or row==z-1 or row+col==z-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
