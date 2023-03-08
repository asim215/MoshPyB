numbers = [1, 2, 3, 3, 5, 2]
uniques = set(numbers)
print(uniques)
second_set = {1, 3, 78, 28}
second_set.add(18)
second_set.remove(3)
print(second_set)
print("lenght ", len(second_set))

# Operations on sets
s1 = {1, 2, 3, 4}
s2 = {2, 4, 5, 6}
print("s1", s1)
print("s2", s2)

print("union", s1 | s2)
print("intersection", s1 & s2)
print("difference", s1 - s2)
print("semantic difference XOR", s1 ^ s2)

if 1 in s1:
    print("yes")
