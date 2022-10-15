"""
    Goal 1
       You first goal is to create a lazy iterator that will produce a named tuple for each row of data
       The content of each row should be an appropriate data type (e.g date, int, string)

       You can use the split method for string on the comma

       You will need to use the strip method to remove the end-of-line character(\n)

       Remember, the goal is to produce a lazy iterator
                -> you should not reading the entire file in memory and the processing it
                -> the goal is to keep the required memory overhead to a minimum
        Stick to python's built-ins and the standard library only! Don't use 3rd parties such as pandas


    Goal 2:
       Calculate the number of violations by car make
       Use the lazy iterator you created in Goal 1
       Use lazy evaluation whenever possible
       You can choose otherwise, but I would store the make and violation counts as dictionary

"""


##################### Goal 1 ###################

file_name = 'nyc_parking_tickets_extract.csv'
with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')
    sample_data = next(f).strip('\n').split(',')

column_names = [header.replace(' ', '_').lower() for header in column_headers]
#print(list(zip(column_names, sample_data)))

from collections import defaultdict, namedtuple
from datetime import datetime
from email.policy import default
Ticket = namedtuple('Ticket', column_names)

def read_data():
    with open(file_name) as f:
        next(f)
        yield from f

def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default

def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default

def parse_string(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except:
        return default


from functools import partial

column_parsers = (
            parse_int,
            parse_string,
            lambda x: parse_string(x, default=''),
            partial(parse_string, default=''), #same as lambda x
            parse_date,
            parse_int,
            partial(parse_string, default=''),
            parse_string,
            lambda x: parse_string(x, default='')
         )


def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    parsed_data = [func(field) 
                    for func, field in zip(column_parsers, fields)]
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    return default

rows = read_data()
for _ in range(5):
    row = next(rows)
    parsed_data = parse_row(row)
    #print((parsed_data), end ='\n\n')


def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed


parsed_rows = parsed_data()
for _ in range(5):
    #print(next(parsed_rows))
    pass 


##################### Goal 2 ###################
makes_counts = {}
for data in parsed_data():
    if data.vehicle_make in makes_counts:
        makes_counts[data.vehicle_make] += 1
    else:
        makes_counts[data.vehicle_make] = 1

#Sorted returns tuples
for make, count in sorted(
                            makes_counts.items(),
                            key= lambda t: t[0],
                            reverse=True):
                            #print(make, count)
                            pass 

# ============== Another approach ================

def violation_count_by_make():
    """Returns the number of violation counts per make"""
    makes_counts = defaultdict(int)

    for data in parsed_data():
        makes_counts[data.vehicle_make] += 1
        
    #Sorted returns tuples
    return {make: count for make, count in sorted(
                    makes_counts.items(),
                    key= lambda t: t[1],
                    reverse=True)
    }

print(violation_count_by_make())
                                


