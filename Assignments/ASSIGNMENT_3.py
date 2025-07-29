n=int(input("Enter total Questions: "))
print("🧪 Welcome to the Python Quiz Game!")
def Q1():
    print('''
Question 1: What is the output of: print(type([]))?
a) <class 'list'>
b) <class 'dict'>
c) <class 'set'>
d) <class 'tuple'>''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='a':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "a"')
        return False
def Q2():
    print('''
Question 2: Which keyword is used to define a function in Python?
a) function
b) def
c) fun
d) define''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='b':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "b"')
        return False
def Q3():
    print('''
Question 3: What is the output of 3 * '5'?
a) 15
b) 555
c) Error
d) None''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='b':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "b"')
        return False
def Q4():
    print('''
Question 4: Which of the following is **immutable**?
a) list
b) dict
c) set
d) tuple''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='d':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "d"')
        return False
def Q5():
    print('''
Question 5: How do you start a comment in Python?
a) //
b) <!--
c) #
d) **''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='c':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "c"')
        return False
def Q6():
    print('''
Question 6: What does len() do in Python?
a) Calculates size of int
b) Returns list length
c) Finds memory usage
d) Loops through list''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='b':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "b"')
        return False
def Q7():
    print('''
Question 7: What is the correct file extension for Python files?
a) .pt
b) .python
c) .py
d) .pyt''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='c':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "c"')
        return False
def Q8():
    print('''
Question 8: Which of the following is used to import a module?
a) include
b) import
c) using
d) require''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='b':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "b"')
        return False
def Q9():
    print('''
Question 9: What is the output of bool(0)?
a) True
b) False
c) 0
d) None''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='b':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "b"')
        return False
def Q10():
    print('''
Question 10: What is used to define a block of code in Python?
a) Brackets {}
b) Parentheses ()
c) Indentation
d) Curly braces''')
    opt=input("Enter your answer(a,b,c,d): ")
    if opt=='c':
        print('✅ Correct!')
        return True
    else:
        print('❌ Wrong! The correct answer is "c"')
        return False
l=[]
for i in range(1,n+1):
    l.append(f'Q{i}()')
    
count=0
for i in l:
    s=eval(i)
    if s:
        count+=1
print()
print(f'🎯 Your Final Score: {count}/10')
if count>=7:
    print("🎉 Great job!! Keep practicing!")
elif 0<count<7:
    print('👍 Good try! Concentrate more!')
else:
    print('👎 Attend and listen classes Consistently,Practice hard!')