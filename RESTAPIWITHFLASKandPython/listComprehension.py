friends = ["Rolf", "Sam", "Samantha", "Jen"]
starts_s = []
for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


starts_with_s = [friend for friend in friends if friend.startswith("S")]

print(starts_with_s)

