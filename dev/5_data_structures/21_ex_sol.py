from pprint import pprint

# Find most repeated character

# Mosh solution
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(sorted(char_frequency.items()))
char_freq_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)
pprint(char_freq_sorted[0])
