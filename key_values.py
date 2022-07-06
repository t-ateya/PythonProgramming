"""
 Iterating over key-value pairs
"""

di = {6:'Max',2:"Bella", 9:'TinTin'}

for i in di.keys():
    print("Keys", i)

for j in di.values():
    print("values: ", j)

for i, j in di.items():
    print(i)
    print(j)

for k in di.values():
    if k == 'Max':
        print("Value matches")

for k in di.keys():
    if di[k]=='Max':
        print("There is a match")