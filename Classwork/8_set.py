#Set Allows only immutable datatypes(list and dict not allowed)

#It supports membership Operators

num={1,2,3,4}
name={'arjun','sarkaar','viraj',4}
print(num|name) #{1, 2, 3, 4, 'viraj', 'sarkaar', 'arjun'} #UNION
print(num&name) #{4} #INTERSECTION
print(num-name) #{1, 2, 3} #DIFFERENCE
print(num^name) #{1, 2, 3, 'sarkaar', 'arjun', 'viraj'} #SYMMETRIC_DIFFERENCE
s1={1,2}
s2={1,2,3}
print(s1<=s2) #True [s1 is subset of s2]
print(s2>=s1) #True [s2 is superset of s1]
s3,s4={1,2},{3,4}
print("s3.isdisjoint(s4):",s3.isdisjoint(s4)) #True If no Common Elements

s={1,2,3,4,5,6}
s.add(7)
s.remove(4) #It removes element,It gives error if element doesn't exist
s.discard(9) #It removes element,It doesn't give error if element doesn't exist
s.pop() #Removes and returns an arbitrary element
s.clear() #clears the values in the set
num.update(name) #Can be called as union_update
num.intersection_update(name) #update num with intersection elements
#Similarly,
num.difference_update(name)
num.symmetric_difference_update(name)
f=frozenset({1,2,3}) #or #frozenset((1,2,3)) #frozenset([1,2,3])
f.add(4) #Error
