number = 100
while number > 0:
    print("before div", number)
    number //= 2
    print("after div", number)


# Condition for exit
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
