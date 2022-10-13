
"""
    yield from is used in Delegating to another iterator

    Simple Syntax
    We can replace an inner loop by using simpler syntax: yield from

    def read_all_data():
        for file in ('file1.csv', 'file2.csv', 'file3.csv'):
            with open(file) as f:
                for line in f:
                    yield line

    def read_all_data():
        for file in ('file1.csv', 'file2.csv', 'file3.csv'):
            with open(file) as f:
                yield from f


"""

def matrix(n):
    gen = (
        (i * j for j in range(1, n+ 1))
        for i in range(1, n+1)
    )
    return gen 

m = list(matrix(5))

#print(m)

def matrix_iterator(n):
    for row in matrix(n):
        for item in row:
            yield item 


def matrix_iterator(n):
    for row in matrix(n):
        yield from row 

for item in matrix_iterator(3):
    #print(item)       
    pass 

file_1 = 'car-brands-1.txt'
file_2 = 'car-brands-2.txt'
file_3 = 'car-brands-3.txt'

all_files = file_1, file_2, file_3

def read_files():
    brands = []

    with open(file_1) as f:
        for brand in f:
            brands.append(brand.strip('\n'))

    with open(file_2) as f:
        for brand in f:
            brands.append(brand.strip('\n'))

    with open(file_3) as f:
        for brand in f:
            brands.append(brand.strip('\n'))
    return brands

brands = read_files()

for brand in brands:
    #print(brand)
    pass 

##### Using a better approach to read files: Generator object approach  #####

def brands(*files):
    """This is an generator obj coz of yield. It returns an iterator"""
    for file in files:
        with open(file) as f:
            for line in f:
                yield line.strip('\n')

for brand in brands(*all_files):
    #print(brand)
    pass 

def gen_clean_data(file):
    with open(file) as f:
        for row in f:
            yield row.strip('\n')

def brands(*files):
    for f_name in files:
        yield from gen_clean_data(f_name)

print(list(brands(*all_files)))

for brand in brands(*all_files):
    print(brand)
    
