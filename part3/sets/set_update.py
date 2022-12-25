
"""
   Sets - Update Operation
   s1 = {1, 2, 3}
   s2 = {2, 3, 4}
"""

s1 = {1, 2, 3, 4}
s2 = {2, 3}
s3 = {3, 4}

#s1 = s1  &  s2 

#print(s1, id(s1))
#print(s2, id(s2))

#s1.difference_update(s2, s3)

#print(s1)

def combine(string, target):
    target.update(string.split(" "))

def cleanup(combined):
    words = {'the', 'and', 'a', 'or', 'is', 'of'}
    combined -= words

result = set()
combine('lumberjacks sleeps all night', result)
combine('the ministry of silly walks', result)
combine('this parrrot is a late parrot', result)

cleanup(result)

#print(result)

def gen_read_data():
    yield ["Paris", "Beijing", "New York", "London", "Madrid", "Mumbai"]
    yield ["Hyderabad", "New York", "Milan", "Phoenix", "Berlin", "Cairo"]
    yield ["Stockholm", "Cairo", "Paris", "Barcelona", "San Francisco"]

def filter_incoming(*cities, data_set):
    data_set.difference_update(cities)


result = set()
data = gen_read_data()

for page in data:
    result.update(page)
    filter_incoming("Paris", "London", data_set=result)
    
print(result)