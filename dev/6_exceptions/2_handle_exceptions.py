# numbers = [1, 2]
# List index out of range
# print(numbers[2])

# Conversion error
# ValueError "i" to int
try:
    age = int(input("Age: "))
    print(f"Your age is {age}")
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution continues")
