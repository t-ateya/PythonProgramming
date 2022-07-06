names = ["John", "Doe"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not Found")

guess = 0
answer = 5
while guess != answer:
    guess = int()
