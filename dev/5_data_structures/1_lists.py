# List unpacking
numbers = list(range(20))

# Unpacking
first, second, *others = numbers
print(numbers)
print(first)
print(second)
print(others)

first, *others, last = numbers
print(numbers)
print(first)
print(last)
print(others)
