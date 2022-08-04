local = {"Rolf"}

abroad = {"Bob", "Anne"}

friends = local.union(abroad)
#print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
either = art.difference(science)

print("both: ", both)
print("either: ", either)