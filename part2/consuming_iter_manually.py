s = 'I sleep all night and I work all day'
iter_s = iter(s)

#print(next(iter_s))

from collections import namedtuple

def cast(data_type, value):
    if data_type == "DOUBLE":
        return float(value)
    elif data_type == 'INT':
        return int(value)
    else:
        return str(value)


def cast_row(data_type, data_row):
    return [cast(data_type, value) 
                    for data_type, value in zip(data_type, data_row)]

def process_data():
    cars = []
    with open('cars.csv') as file:
        row_index = 0
        for line in file:
            #print(line, end ="")
            if row_index == 0:
                # header row
                headers = line.strip('\n').split(";")
                #print("headers: ", headers)
                Car = namedtuple('Car', headers)
            elif row_index == 1:
                #data type row
                data_types = line.strip("\n").split(";")
                #print("type: ", data_types)
            else:
                #data row
                data = line.strip("\n").split(";")
                data = cast_row(data_types, data)
                car = Car(*data)
                cars.append(car)
                #print("data: ", data)
            row_index += 1
    return cars

#print(process_data())

#Another approach using iterator

def read_and_process_data():
    cars = []
    with open("cars.csv") as file:
        file_iter = iter(file)  #file object is an iterable. We need to call the iterator, iter() on file
        headers = next(file_iter).strip("\n").split(";") #first row
        Car = namedtuple('Car', headers)
        data_types = next(file_iter).strip("\n").split(";") #2nd row
        
        #Then loop through the rest of the data start from 3rd row

        for line in file_iter:
            data = line.strip("\n").split(";")
            data = cast_row(data_types, data)
            car = Car(*data)  #make new namedtuple out of the data
            cars.append(car)

    return cars

#print(read_and_process_data())

def read_and_process_data_better_approach():
    with open("cars.csv") as file:
        file_iter = iter(file)  #file object is an iterable. We need to call the iterator, iter() on file
        headers = next(file_iter).strip("\n").split(";") #first row
        Car = namedtuple('Car', headers)
        data_types = next(file_iter).strip("\n").split(";") #2nd row
        
        #Then loop through the rest of the data start from 3rd row
        cars = [Car(*cast_row(data_types, line.strip("\n").split(';'))
        
                        )
                    for line in file_iter]
    
    return cars

print(read_and_process_data_better_approach())
            
