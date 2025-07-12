num=int(input("Enter the integer: "))
print(num)

f_num=float(input("Enter the float num: "))
print(f_num)

names=input("Enter the names: ").split() #Enter the names: MyName YourName
#For Strings
print(names) #['MyName', 'YourName']

num = list(map(int,input("Enter the nums: ").split())) #For numbers
print(num) #[1,2,3,4]


num = list(map(int,input("Enter the nums: ").split()))
print(num)

dic=eval(input("Enter the dict: "))
print(dic) #{'name':'xyz','age':99}

name,email,pswrd=input("Enter the data: ").split()
print(name) #hii
print(email) #hii@gmail.com
print(pswrd) #hii1234

a,b,c=1,2,3
print("a:",a,"b:",b) #a: 1 b: 2

print(f'a:{a}\nb:{b}')
#a:1
#b:2

a=1
b=2
print('a:{}\tb:{}'.format(a,b)) #a:1   b:2

print(a,end=",")
print(b) #2,3

a=1
b=1.2
print('a:%d,b:%.1f'%(a,b)) #a:1,b:1.2
