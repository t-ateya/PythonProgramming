
import random

class RandomNumbers:
    def __init__(self, length, *, range_min = 0, range_max = 10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.number_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.number_requested >= self.length:
            raise StopIteration
        else:
            self.number_requested +=1
            return random.randint(self.range_min, self.range_max)


numbers = RandomNumbers(5)

while True:
    try:
        print(next(numbers))
    except StopIteration:
        break 


for n in numbers:
    print(n)