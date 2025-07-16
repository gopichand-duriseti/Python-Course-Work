v=int(input("Enter rows for V pattern: "))
for row in range(v):
    for col in range(v):
        if (col in (0,v-1) and row in range(0,v//2+1)) or (row==v-1 and col==v//2) or ((row-col==v//2 or (row+col)/3==v//2) and row in range(v//2+1,v-1)):
        #row==a//2 or (col==a//2 and row==0) or (row+col==a-1 and row in range(1,a//2)) or (row==col and row in range(1,a//2)) or (col==0 and row in range(a//2+1,a)) or (col==a-1 and row in range(a//2+1,a)):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()