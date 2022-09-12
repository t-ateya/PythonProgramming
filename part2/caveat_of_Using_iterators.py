


import random 
class Randoms:
    def __init__(self, n):
        self.n = n 
        self.i = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            self.i += 1
            return random.randint(0, 100)

random.seed(0)
l = list(Randoms(10))
#print(l)

#print(min(l), max(l))
random.seed(0)
l = Randoms(10)

#print(min(l))

#print(max(l))

def parse_data_row(row):
    row = row.strip('\n').split(';')
    return row[0], float(row[1])

def max_mpg(data):
    max_mpg = 0
    for row in data:
        _, mpg = parse_data_row(row)
        max_mpg = mpg if mpg > max_mpg else max_mpg
    return max_mpg


def list_data(data, mpg_max):
    for row in data:
        car, mpg = parse_data_row(row)
        mpg_perc = mpg / mpg_max * 100
        print(f"{car}: {mpg_perc:.2f}%")

"""
f = open("cars.csv")
next(f), next(f)
list_data(f, 46.6)
f.close()
"""
with open("cars.csv") as f:
    '''Problem with this code coz the iterator gets consumed'''
    next(f)
    next(f)
    #list_data(f, 46.6)
    max_ = max_mpg(f) #f get's exhausted here since it an iterator 
    #print(max_)
    list_data(f, max_) # f is empty since it already got exhausted in the max_mpg(f) call above

"""The problem above can be fixed below with the following approaches"""

#Approach 1 : Loading the data into memory
with open('cars.csv') as f:
    cars = f.readlines()[2:] #start reading lines from index 2
    #The cons with this method is that if loads all the data and stores in memory thereby consuming the memory. Hence, inefficient

max_ = max_mpg(cars)
#list_data(cars, max_)

#Approach 2: Opening the file twice 

with open('cars.csv') as f:
    next(f), next(f)
    max_ = max_mpg(f)


with open('cars.csv') as f:
    next(f), next(f)
    #list_data(f, max_)

#Combining everying in one function
def proces_data(data):
    if iter(data) is data:
        data = list(data)
        
    max_mpg = 0
    for row in data:
        _, mpg = parse_data_row(row)
        max_mpg = mpg if mpg > max_mpg else max_mpg

    for row in data:
        car, mpg = parse_data_row(row)
        mpg_perc = mpg / max_mpg * 100
        print(f"{car}: {mpg_perc:.2f}%")

with open('cars.csv') as f:
    next(f), next(f)
    proces_data(f)

    

