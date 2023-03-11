from sys import getsizeof

# Using List to store into memory
values_l = [x**2 for x in range(2000)]
for x in values_l:
    print(x)
# Using Generator Expressions - gen on the go
values_g = (x**2 for x in range(2000))
for x in values_g:
    print(x)

# size of obj
print(
    f"Size of {type(values_l)} list {getsizeof(values_l)}, \
    of {type(values_g)} generator object {getsizeof(values_g)}"
)
