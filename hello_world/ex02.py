# for number in range(3):
# for number in range(1, 4):
for number in range(1, 10, 2):
    # print("Attempt", number + 1, (number + 1) * ".")
    print("Attempt", number, number * ".")

# FOR ELSE
# Successful send then out of loop
# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break

# For else
print(">For Else")
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
# if try 3 times and unsuccessful
else:
    # if never use break from loop then else
    print("Attempted 3 times and failed")
