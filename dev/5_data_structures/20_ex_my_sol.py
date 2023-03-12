# Find most repeated character

# My solution
sentence = "This is a common interview question"
frequency = {}
for letter in sentence:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

highest_freq = 0
highest_letter = ""
for letter, number in frequency.items():
    if number > highest_freq:
        highest_freq = number
        highest_letter = letter

print(f"Most repeated character is {highest_letter} it appear {highest_freq} times")
