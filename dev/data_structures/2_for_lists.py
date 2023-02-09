# Looping over Lists
letters = list(range(20, 50, 2))

for letter in letters:
    print(letter)

# Enumerate with index. Get tuple
for letter in enumerate(letters):
    print(letter)
    print(f"{letter[0]} <> {letter[1]}")

# Tuple unpacking
for index, letter in enumerate(letters):
    print(index, letter)
