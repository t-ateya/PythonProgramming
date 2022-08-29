
"""
for x in range(5):
    print(x);

for i in 'python':
    print(i);

li = [1,2,3,4,5,6]
sum = 0;

for x in li:
    sum+=x;
print(sum);

#range (start, end)
for i in range(10, 25):
    print(i)

#range(start, end, step_size)
for x in range(10,25, 2):
    print("x: ",x)

for x in range(25, 10,-2):
    print("desc", x)


#number of odd and even numbers

list_number= list(range(100))
number_even = 0;
number_odd = 0
for i in range(100):
    if i%2 == 0:
        print("The number is even: ", i)
        number_even+=1
    else:
        print("The number is odd: ",i)
        number_odd+=1

    
#print("There are: %i number of even elements", number_even);

for i in 'python':
    if i =='o':
        break
    print("break statement", i)

for i in 'python':
    if i =='o':
        continue
    print("continue statement", i)

"""

li = list(range(50))
tup = tuple(range(50))
se = set(range(50))

for i in li:
    print("list: ", i)

for i in tup:
    print("tuple:", i)

for i in se:
    print("set: ", i)

