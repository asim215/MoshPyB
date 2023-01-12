# Ternary
age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

message = "Eligible" if age >= 18 else "Not eligible"

print(message)

# Chaining comparison operators
age = 22
if 18 <= age < 65:
    print("Eligible")
