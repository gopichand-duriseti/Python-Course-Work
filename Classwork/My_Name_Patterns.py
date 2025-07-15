o_g=int(input("Enter rows for other G pattern: "))
for row in range(o_g):
    for col in range(o_g):
        if row==0 or col==0 or row==o_g-1 or (col in range(o_g//2,o_g) and row == o_g//2) or (row in range(o_g//2+1,o_g-1) and col==o_g-1):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print() 
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
i=int(input("Enter rows for I pattern: "))
for row in range(i):
    for col in range(i):
        if row==0 or row==i-1 or col==i//2:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()
