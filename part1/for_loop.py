
for i, j in [(1,2), (3, 4), (5, 6)]:
    print(i,j)

for i in range(5):
    if i == 3:
        continue
    print(i)


s = "hello"
for index, c in enumerate(s):
    print(index,c)