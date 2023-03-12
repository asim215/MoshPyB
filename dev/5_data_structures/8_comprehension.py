items = [
    ("ProductName1", 82),
    ("ProductName2", 34),
    ("ProductName3", 72),
    ("ProductName1", 52),
    ("ProductName2", 4),
    ("ProductName3", 22),
]

# x = filter(lambda item: item[1] >= 50, items)
# print(x, hex(id(x)), type(x))
# print(list(x))

# Comprehension
prices = [item[1] for item in items]
# Same as
# list(map(lambda item: item[1], items))

filtered = [item for item in items if item[1] >= 50]

print("Prices: ", prices)
print("Filtered: ", filtered)
