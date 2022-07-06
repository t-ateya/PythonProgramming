numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
#print(new_list)

###List Comprehension
#print([x+1 for x in numbers])
#[print(x+1) for x in numbers]

#another_list = [n + 1 for n in numbers]
#print(another_list)

name = "Angela"
new_list = [letter for letter in name]
#print(new_list)

range_list = [x*2 for x in range(1,5)]
#print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]

new_names_list = [name for name in names if len(name)<=4 ]
#print(new_names_list)

upper_case_list = [name.upper() for name in names if len(name)>=5]
print(upper_case_list)