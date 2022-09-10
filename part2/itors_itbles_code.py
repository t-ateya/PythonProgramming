
class Cities:
    def __init__(self):
        self._cities = ["Paris", "Berlin", "Rome", "Madrid", "London"]
        self._index = 0

    def __len__(self):
        return len(self._cities)

    #Iterable protocol: Iterables do not get consumed because they return a new instance of the iterable every time
    def __iter__(self):
        print("Cities __iter__ called")
        return self.CityIterator(self)

    #Let's make Cities a sequence class
    def __getitem__(self, s):
        return self._cities[s]


    #Iterable
    class CityIterator:
        def __init__(self, city_obj ) -> None:
            print("CityIterator new object:")
            self._city_obj = city_obj
            self._index = 0

        #Iterator Protocol: Iterators get consumed because they return themselves
        def __iter__(self):
            print("CityIterator __iter__ called")
            return self 

        def __next__(self):
            print("CitiesIterator __next__ called")
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item



"""

cities = Cities()

print(list(enumerate(cities)))
#next(cities)
print(list(enumerate(cities)))

cities = Cities()
print([item.upper() for item in cities])

print(len(cities))
"""

cities = Cities()

"""
city_iterator = CityIterator(cities)

for city in city_iterator:
    #print(city)
    pass 

for city in cities:
    print(city)
    


city_iter_1 = cities.__iter__()
city_iter_2 = cities.__iter__()
city_iter_3 = cities.__iter__()

for city in city_iter_1:
    print(city)

print("===========================")
for city in city_iter_1:
    print(city)
"""


#print(list(enumerate(cities)))

#print(sorted(cities, key=lambda city: len(city)))

s = {'a', 100, 'x', 'y', 'a'}

set_iterator = iter(s)

for item in set_iterator:
    #print(item)
    pass 

print(cities[::-1])
print(cities[0])
print(cities[-1])
