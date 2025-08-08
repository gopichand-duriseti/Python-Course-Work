#Reverse Every Word in a Sentence
def reverse_wrd():
    print('Code:')
    print('''def reverse_wrd(s):
    rev=''
    for i in s.split():
        rev+=i[::-1]+' '
    print(rev)
TestCases:
reverse_wrd(input('Hello World')):-olleH dlroW
reverse_wrd(input('I am gopi chand')):-I ma ipog dnahc
Explaination:
In this code,we used slicing method to reverse and split() method to get each word and adding to a new variable containing empty string to get required output
''')

#Print Emoji Triangle
def emoji():
    print("Code:")
    print('''def emoji(emoji,n):
    for i in range(1,n):
        print(emoji*i)
TestCases
emoji('😁',6):-
😁
😁😁      
😁😁😁    
😁😁😁😁  
😁😁😁😁😁
emoji('😊',3):-
😊
😊😊
Explaination:
Here, We used emoji,rows lenght as input() inside function and with the help of for loop iteration done accordingly to print emoji triangle
''')
    
#Convert Decimal to Binary (without bin())
def dec_bin():
    print('Code:')
    print('''def dec_bin(decimal):
    b=''
    while decimal>0:
        b+=str(decimal%2)
        b=b//2
    print(b)
TestCases:
dec_bin(5): 101
dec(62): 11110
Explaination:
Here we used modulus operator(to get reminder) and floor division operator(to get whole numbers) and assigning the whole number again and again after every iteration to the variable storing empty string taken before while loop and by reversing(reverse slicing) reminders we will get the binary number
''')
#Number of Days Between Two Dates
def date_diff():
    print('Code:')
    print('''def date_diff(d1,d2):
    from datetime import datetime
    diff = abs((datetime.strptime(d2, "%Y-%m-%d") - datetime.strptime(d1, "%Y-%m-%d")).days)
    print("Days between:", diff)
d1 = input("Start date (YYYY-MM-DD): ")
d2 = input("End date (YYYY-MM-DD): ")
TestCases:
date_diff('2011-05-20','2012-09-23'):Days between: 492
date_diff('2025-02-27','2023-07-14'):Days between: 594
''')
date_diff()