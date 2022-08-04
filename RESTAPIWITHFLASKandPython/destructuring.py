people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for person in people:
    print(person)

print("=====================================")
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

print("***************************************")

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


_person = ("Bob", 42, "Mechanic")
name, _, profession = _person
print(name, profession)

head, *tail = [1, 2, 3, 4]
*others, last = [4,3,5,6,7,9]

print(head)
print(tail)

print(*others)
print(last)
