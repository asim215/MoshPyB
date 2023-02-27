items = [
    ("ProductName1", 82),
    ("ProductName2", 34),
    ("ProductName3", 72),
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)
# Map
x = map(lambda item: item[1], items)

# for item in x:
#     print(item)

# Convert to list
print(list(x))
