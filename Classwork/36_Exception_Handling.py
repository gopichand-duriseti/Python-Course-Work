print("Exception Handling".center(50,'-'))
#Exception Handling is uded to handle RUNTIME ERRORS
'''if 2%2==0:
print(True) #Syntax Error'''
'''12/0---ZeroDivisionError'''
'''age=int(input()) :-ncjkkf ----ValueError'''
'''12+"13"----TypeError'''
'''l=[1,2,3],l[12]----IndexError'''
'''k[0]----NameError(k is not defined)'''
#Random Program:-print(True) if 2 % 2== 0 else print(False) or print(2%2==0)
'''x={'hi':1,'hello':2},x['himmm'])----KeyError'''
'''
try:
    print(k)
    x=int(input("Enter x: "))
    y=int(input("Enter y: "))
    d={"hi":1,"hello":2}
    d[input("Enter Key: ")]
    l=[1,2,3,4,5]
    ind=int(input("Enter the index value: "))
    print(l[ind])          
    print(x+y)
    print(x/y)
except Exception as e:
    print(e)
except (ZeroDivisionError,ValueError,TypeError,IndexError,KeyError,NameError) as e:
    print(f'Error occured:{e}')
except ZeroDivisionError:
    print("b cannot be zero")
except ValueError:
    print("Please enter integer value only")
except TypeError:
    print("Please enter same type")
except IndexError:
    print("Enter the index within the range")
except KeyError:
    print("Enter the Existed Key or Key is not present")
else:
    print("All inputs are perfect no exceptions you can run remaining code")
finally:
    print(x,y,l) #nameerror for l if key entered is not there in dict "d" because l is not defined before d

'''



try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    op=input("Enter the operation: ")
    
    if a<0:
        raise Exception("please enter postive number")
    if b==0 and op=="a/b":
        raise Exception("b cannot be zero")
except Exception as e:
    print(e)
    print(a,b)
else:
    print("All inputs are perfect no exceptions you can run remaining code")
        
