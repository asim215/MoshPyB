values = []
for x in range(5):
    values.append(x * 2)
# can be replaced with
# map()
# or
# list comprehension
print(values)

# [expression for item in items]
values = [x * 2 for x in range(5)]
print(values)
# set
values = {x * 2 for x in range(5)}
print(values)

# dicts
values = {x: x * 2 for x in range(5)}
print(values)
