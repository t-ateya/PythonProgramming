
import random

random.seed(0)

for _ in range(10):
    #print(random.randint(1,10))
    pass 


class RandomInts:
    def __init__(self, length, *, seed=0, lower=0, upper=10):
        self.legth = length
        self.seed = seed 
        self.lower = lower 
        self.upper = upper

    def __len__(self):
        return self.legth

    def __iter__(self):
        return self.RandomIterator(self.legth, seed=self.seed, lower=self.lower, upper=self.upper)

    class RandomIterator:
        def __init__(self, length, *, seed, lower, upper):
            self.length = length 
            self.lower = lower 
            self.upper = upper 
            self.num_requests = 0
            random.seed(seed)

        def __iter__(self):
            return self 

        def __next__(self):
            if self.num_requests >= self.length:
                raise StopIteration
            else:
                result = random.randint(self.lower, self.upper)
                self.num_requests += 1
                return result

randoms = RandomInts(10)

"""
for nums in randoms:
    print(nums)


print([nums for nums in randoms])
"""


"""
print("=========seed set to 0 ================")

randoms = RandomInts(10, seed=None)
for nums in randoms:
    print(nums)

print([nums for nums in randoms])
"""

print(list(randoms))
print(sorted(randoms))
print(sorted(randoms, reverse=True))