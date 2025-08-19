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
