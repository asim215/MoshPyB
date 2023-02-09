# List unpacking
numbers = list(range(20))
print(numbers)

first, second, *others = numbers
print(first)
print(second)
print(others)

first, *others, last = numbers
print(first)
print(last)
print(others)
