a = {'a':1,'b':2,'c':3}
#print (a['a','b'])  #Key error


arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1
 
sum = 0
for k in arr:
    sum += arr[k]
 
#print(sum)


dict = {'c': 97, 'a': 96, 'b': 98}
 
for _ in sorted(dict):
    print (dict[_])



rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
#print(id1 == id2)


rec = {"Name" : "Python", "Age":"20"}
r = rec.copy()
#print(id(r) == id(rec))


box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
#print(len(crates[box]))



my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4
 
sum = 0
for k in my_dict:
    sum += my_dict[k]
    
#print (sum)


a = {(1,2):1,(2,3):2}
#print(a[1,2])



fruit = {}
 
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
        
addone('Apple')
addone('Banana')
addone('apple')
#print (len(fruit))



my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
 
sum = 0
for k in my_dict:
    sum += my_dict[k]
 
print(sum)
print(my_dict)