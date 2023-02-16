# def multiply(x, y):
#     return x * y

# Variable number of parameters
# by tuple, iterable
def multiply(*numbers):
    # print(numbers)
    total = 1
    for number in numbers:
        total *= number
        # print(number)
    # return x * y
    return total


print(multiply(2, 3, 4, 5))
