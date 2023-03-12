point = 1, 2  # tuple
print("1, 2", type(point))
point = (1, 2)  # tuple
print("(1, 2)", type(point))

point = 1  # integer
print("1", type(point))
point = (1,)  # tuple
print("1,", type(point))

# Concatenate
point = (1, 2) + (3, 4)
print("Concatenate ", point)

# Repeat
point = (1, 2) * 4
print("Repeat ", point)

# Convert
point = tuple([1, 2, 3])
print("tuple list ", point)

point = tuple(range(10))
print("tuple range ", point)

point = tuple("Hello world arount us")
print("tuple string ", point)
print("tuple string slice", point[3:10])

# Unpack
x, y, z = tuple(range(3))
print("unpacked", x, y, z)
if "w" in point:
    print("exists")
# Immutable
point[0] = "W"
