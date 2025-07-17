#Square numbers in a range:
squares = [x * x for x in range(6)]
print(squares)

#Filter even numbers:
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)

#Uppercase a list of strings:
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)
