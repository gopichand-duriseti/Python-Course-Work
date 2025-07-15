#NESTED LOOPS means loop within the loop

#OUTER LOOP means 'rows' and INNER LOOP means 'columns'

for row in range(5):
    for column in range(5):
        print(f"*",end=" ")
    print()