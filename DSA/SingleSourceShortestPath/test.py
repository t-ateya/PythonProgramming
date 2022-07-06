from collections import defaultdict
new_dict = defaultdict(set)
new_dict1 = defaultdict(list)
new_dict2 = defaultdict(dict)
new_dict["age"] = 28
new_dict["eye"] = "brown"
new_dict["sex"].add(30)
new_dict["sex"].add(31)
new_dict["sex"].add(31)

new_dict1["love"].append("I")
new_dict1["love"].append("Love")
new_dict1["love"].append(31)
new_dict1["friend"].append("Kelly")
new_dict1["friend"].append("Kelly")


#[print(d) for d in new_dict]
print(new_dict)
print(new_dict1)