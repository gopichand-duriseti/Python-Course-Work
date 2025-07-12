l=[1,2,3,4,5,6,7]
print(l[-4:]) #[4,5,6,7]
print(l.pop(2)) #3
x=1
b='helo'
s=[]
print(all((x,b,s))) #False
print(any((x,b,s))) #True
l=[0,1,2,3]
print(any(l)) #True
print(all(l)) #False
print(l.sort(reverse=True)) #[7,6,5,4,3,2,1] #It Modifies the list "l"
print(sorted(l)) #[1,2,3,4,5,6,7] #It doesn't Modifies the list "l"
#Two types of copies:Shallow copy(It doesn't effect the original list,term used:c=ol.copy()) and deep copy(c=ol,effects the list 'ol')
