import re

res=re.match("Hello","Hello world")
print(res) #<re.Match object; span=(0, 5), match='Hello'>
print(res.group() if res else "No Match") #Hello

res=re.match(r'\d','8Hello World')
print(res.group() if res else "No Match") #8
res=re.match(r'\d','Hello World')
print(res.group() if res else "No Match") #No Match

print(re.match(r'[0-9]','5678Hello'))
print(re.match(r'[A-Z]','ASello'))
print(re.match(r'[a-z]','aeHello'))
print(re.match(r'[6-9]','9879405')) #if number starts with number>=6 and number<=9

'''re.search()'''
print(re.search(r'h.t','hit hat hit'))

'''re.findall()'''
print(re.findall(r'h.t','hit hat hot'))

'''re.finditer()''' #It is a lazy loading where it executes value one by one
res=re.finditer(r'[0-9]','Hello world 76 34 90 23') 
for i in res:
    print(i.group(),i.start()) #i.start is used to know the index/position of that character

res=re.finditer(r'[0-9]{2}','Hello world 76 34 90 23')  #length of number should be 2
for i in res:
    print(i.group(),i.start())

res=re.fullmatch(r'[0-9]{10}','9392375981') #length should be given to get result
print(res.group() if res else "No Match")

res=re.split(r'[,:/0]','1,23045:60708/9') 
print(res) #['1', '23', '45', '6', '7', '8', '9']

res=re.split(r'[,:/0]','1,230450:60708/9') 
print(res) #['1', '23', '45', '', '6', '7', '8', '9']

text='JFS Course'
res=re.sub('JFS',"PFS",text) #replacing
print(res)

res=re.sub(r'[aeiou]','*',text) #or res=re.sub(r'[A-Z]','*',text)
print(res)

'''BASIC METACHARACTERS'''
text='Sanjay is a good boy.He lives in KPHB. Heart Hacker Sanjay.He lovs food.Everyone loves Sanjey.Sanjay number is 9989888908'
res=re.findall(r'.anj.y',text) #['Sanjay', 'Sanjay','Sanjey','Sanjay']
res=re.findall(r'^[A-Z]',text) #['S']
res=re.findall(r'[0-9]$',text) #['8']

'''* Matches 0 or more occurrences ab* → Matches "a", "ab","abb"'''
def validate_name(name):
    pattern=r'^[A-Z][a-z]{2,25}( [A-Z][a-z]{2,25})+$'
    return bool(re.fullmatch(pattern,name))
'''while True:
    print(exit() if validate_name(input("Enter name: ")) else "Wrong Input")'''

def validate_email(email):
    pattern=r'^[A-Za-z0-9]+@[a-z.-]+\.[a-z]{2,3}$'
    return bool(re.fullmatch(pattern,email))
'''while True:
    print(exit() if validate_email(input("Enter email: ")) else "Wrong Input")'''

def validate_phone_number(number):
    pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
    return bool(re.fullmatch(pattern,number))
'''while True:
    print(exit() if validate_phone_number(input("Enter phone number: ")) else "Wrong Input")'''
