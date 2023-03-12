numbers = [3, 34, 82, 182, 31, -8]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# Creates new instance
s = sorted(numbers)
print(s)

print(f"id numbers: {id(numbers)}\nid sorted: {id(s)}")

# Sorting complex objects

# Product Name, Price
items = [
    ("ProductName1", 100),
    ("ProductName2", 23),
    ("ProductName3", 57),
    ("ProductName4", 73),
    ("ProductName5", 10),
]


# Sorting function
# based on price
def sort_item(item):
    # return number to sort
    return item[1]


items.sort(key=sort_item)
print(f"func on obj {id(items)} ", items)

# Usage of lambda

items.sort(key=lambda item: item[1])
print(f"lambda on object {id(items)}", items)
