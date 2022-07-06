# Write a program that shows the most repeated chars in the sentense below
from pprint import pprint
sentense = "This is a common interview quetion"

char_frequency = {}
for char in sentense:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
#pprint(char_frequency, width=1)
char_freq_sorted = sorted(char_frequency.items(),
                          key=lambda kv: kv[1],
                          reverse=True)
print(char_freq_sorted[0])
