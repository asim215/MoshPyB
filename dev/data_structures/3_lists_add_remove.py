letters = ["a", "b", "c"]

# Add
letters.append("d")
print("append", letters)
letters.insert(1, "#")
print("insert", letters)

# Remove
letters.pop()
print("pop", letters)
letters.pop(0)
print("pop0", letters)
letters.remove("b")
print("remove", letters)
numbers = list(range(1, 30))
print(numbers)
del numbers[5:10]
print(numbers)
numbers.clear()
print(numbers)
