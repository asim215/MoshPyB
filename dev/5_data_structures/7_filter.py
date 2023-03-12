items = [
    ("ProductName1", 82),
    ("ProductName2", 34),
    ("ProductName3", 72),
    ("ProductName1", 52),
    ("ProductName2", 4),
    ("ProductName3", 22),
]

x = filter(lambda item: item[1] >= 50, items)
print(x, hex(id(x)), type(x))
print(list(x))
