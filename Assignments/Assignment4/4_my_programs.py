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
#TestCases
emoji('😁',6):-
😁
😁😁      
😁😁😁    
😁😁😁😁  
😁😁😁😁😁
emoji('😊',3):-
😊
😊😊
''')