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