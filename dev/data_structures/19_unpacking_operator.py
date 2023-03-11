numbers = [1, 2, 3]
print(numbers)

values = list(range(5))
print(values)
# unpack iterable
values = [*range(5)]
print(values)
# unpacking string
values = [*range(5), *"Hello"]
print(values)

# Compbine multiple lists
first = [1, 2, 3]
second = [4, 5, 6]
values = [*first, "aa", *second, *"his"]
print(values)

# Unpacking dictionaries
first = {"x": 1}
second = {"x": 10, "y": 8}
combined = {**first, **second, "z": 11}
print(combined)
