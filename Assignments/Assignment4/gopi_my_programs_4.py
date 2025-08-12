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
    print('''def emoji_triangle(emoji,n):
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
Here, We used emoji,rows lenght as input() inside function and with the help of for loop iteration done accordingly to print emoji right angle triangle
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
Explaination:
The given Python code defines a function date_diff that calculates the absolute number of days between two dates provided in the YYYY-MM-DD format. It uses the datetime.strptime method to convert the input strings into datetime objects and then computes the difference between them.
''')
    
#Python Program to Find Largest element an Array
def large_ele():
    print('Code:')
    print('''def largest(arr):
    max_val = arr[0]
    for num in arr[1:]:
        if type(num)==int:
            if num > max_val:
                max_val = num
    print(max_value)
from array import array
Test Cases:
array('i', [10, 324, 45, 90, 9808]):9808 # 'i' = integer array
array('i', [1,2,22,4221,12343,987,123]):12343
Explaination:
This code defines a function that loops through all elements of a list, comparing each to the current maximum and updating it when a larger value is found.It then calls this function with a given list of numbers and prints the largest value.
''')

#Count the Number of matching characters in a pair of string
def count_matches():
    print("Code:")
    print('''def no_of_matches(s1,s2):
    from collections import Counter
    c1 = Counter(s1.lower())
    c2 = Counter(s2.lower())
    matches = sum(min(c1[ch], c2[ch]) for ch in c1 if ch in c2)
    print(matches)
TestCases:
no_of_matches(GOPICHand,gopiChanuu):8
no_of_matches(hey mister,hello brother):6
Explaination:
This code lowercases both strings, counts the frequency of each character using Counter, and finds characters common to both.
It then sums the smallest count for each common character to get the total matching characters (including duplicates).
''')

#Generate a Table of Squares
def sqrs():
    print("Code:")
    print('''def table_squares(l):
    for i in l:
        print(f'{i}:{i**2}')
Testcases:
table_squares([1,3,5,7])
1
9
25
49
table_squares([11,13,19,32])
121
169
361
1024
Explaination:
ChatGPT said:
This function loops through each number in the list l and calculates its square using i**2.
It then prints the number and its square in the format number:square using an f-string.''')

#Check if binary representations of two numbers are anagram
def bin_anagram():
    print("Code:")
    print('''def binary_anagram(b1,b2):
    b1=bin(b1)[2:]
    b2=bin(b2)[2:]
    s1=''.join(sorted(str(b1)))
    s2=''.join(sorted(str(b2)))
    if s1==s2:
        print('The binary representations of the numbers are anagrams')
    else:
        print('The binary representations of the numbers are not anagrams')
TestCases:
binary_anagram(5,6):The binary representations of the numbers are anagrams
binary_anagram(18,23):The binary representations of the numbers are not anagrams
Explaination:
This function converts two numbers to their binary strings (without the 0b), sorts the bits in each, and compares them.
If the sorted bit patterns match, it prints that the binary representations are anagrams; otherwise, it says they are not.''')

#Sort a List of Tuples by Second Item
def sort_tuple():
    print("Code:")
    print('''def sort_tuple_seconditem(t):
    res = sorted(t, key=lambda x: x[1])
    print(res)
TestCases:
sort_tuple_seconditem([(1, 3), (4, 1), (2, 2)]):[(4, 1), (2, 2), (1, 3)]
sort_tuple_seconditem([('a', 5), ('b', 1), ('c', 3)]):[('b', 1), ('c', 3), ('a', 5)]
Explaination:
This function sorts a list of tuples based on the value of their second element using sorted() with a lambda x: x[1] key.
It then prints the sorted list in ascending order of the second item in each tuple.''')

#Printing alphabet "D" star pattern with integer input as rows length
def pattern():
    print("Code:")
    print('''def letter_pattern(row_length):
    d=row_length
    if d>=3:
        for row in range(d):
            for col in range(d):
                if (row==0 and col!=d-1) or (row==d-1 and col!=d-1) or col==0 or (col==d-1 and row not in (0,d-1)):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
            print()
    else:
        print("row length should be greater than or equal to 3")
TestCases:
letter_pattern(5)
* * * *   
*       * 
*       * 
*       * 
* * * *
letter_pattern(8)
* * * * * * *   
*             * 
*             * 
*             * 
*             * 
*             * 
*             * 
* * * * * * *  
Explaination:
This function prints a star pattern based on a given row_length that visually resembles the letter C.
It uses nested loops to iterate through rows and columns, printing * for the top row, bottom row, left column, and right column (except corners on the top and bottom).
Spaces are printed elsewhere to maintain the shape, and it only works if row_length >= 3; otherwise, it shows an error message.''')