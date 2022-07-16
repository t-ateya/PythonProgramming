"""
    #146
    Design and implement a structure for a Least Recently Used (LRU) cache. It should support the get and put operations.
    - get(key) : Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1
    - put(key, value) : insert the value if the key is not already present. Update the value if the key is already present.
    - When the cache reaches its capacity, put(key, value) should invalidate the least recently used item before inserting a new item.

    A cache is a memory that stores data for it to be served faster in the future. Least Recently Used(LRU) is a policy that is used
    to remove items from the cache.

    Solution:
    Data Structure to be used
    - dequeue and map

"""
from collections import deque

class LRUCache:
    def __init__(self, capacity:int):
        self.cap = capacity
        self.m = dict()
        self.deq = deque()

    def get(self, key:int) ->int:
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key) #Verify
            return value
        else:
            return -1
            

    def put(self, key:int, value:int)->None:
        #Case 1: key not in the map
        if (not key in self.m):
            if (self.cap == len(self.deq)):
                oldest = self.deq.popleft()
                del self.m[oldest]      
        else:
            #Update the value 
            self.deq.remove(key)

        self.deq.append(key)
        self.m[key] = value

s = LRUCache(3)

s.put(1, 1000)
s.put(2, 2000)
s.put(3, 3000)

print(s.get(1))

print(s.get(2)) 

s.put(4, 4000)

print(s.get(3))

