student = {
"name": "Alice",
"age": 21,
"course": "Computer Science"
}
print(student.get("age")) #21
'''
Difference Between dict[key] and dict.get(key)
● dict[key] will raise a KeyError if the key does not exist.
● dict.get(key, default_value) will return None or the specified
default_value if the key is not found.'''
print(student.get("city","Not Mentioned")) # Output: Not Mentioned

student["age"] = 22 # Updating existing key
student["city"] = "New York" # Adding a new key-value pair

'''Using pop(key)
Removes the specified key and returns its value.'''
age = student.pop("age")

'''Deletes a specific key-value pair or the entire dictionary.'''
del student["course"]

'''Removes and returns the last inserted key-value pair.'''
student.popitem()

student.clear() #{}

d={1:'hello',2:"hii"}
d.update({"city":"vij"}) #{1: 'hello', 2: 'hii', 'city': 'vij'}
d.setdefault("city","hyd") #{1: 'hello', 2: 'hii', 'city': 'vij'}
#If there is already a value for a key then set default doesn't work
d.update({"city":"vij"}) #{1: 'hello', 2: 'hii', 'city': 'vij'}

'''NESTED DICTIONARY'''
students = {
"Alice": {"age": 21, "course": "CS"},
"Bob": {"age": 22, "course": "Math"}
}
print(students["Alice"]["course"]) #CS

'''DICTIONARY COMPREHENSION'''
squares = {x: x*x for x in range(1, 6)}
print(squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
