
class HashTable:
    def __init__(self):
        self.table_size = 10
        self.arr = self.table_size*[None]
        #self.arr = [None for i in range(self.table_size)]

    def get_hash(self, key):
        """Returns the hash of a given key"""
        sum = 0
        for ch in key:
            sum += ord(ch) #ord(key) converts ascii string to integers
        return sum % self.table_size

    def __setitem__(self, key, value):
        """This function adds data at a specific index in an array"""
        hash = self.get_hash(key)
        self.arr[hash] = value

    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]

    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None 




newHash = HashTable()
#print(newHash.get_hash("march 6"))
"""
newHash.add_hash("Apple", 130)
newHash.add_hash("Orange", 120)
newHash.add_hash("Bananas", 100)
newHash.add_hash("Pear", 12)
    https://www.youtube.com/watch?v=54iv1si4YCM Video link
"""

newHash["Apple"]=130
newHash["Orange"] =120
newHash["Bananas"] = 100
newHash["Pear"] = 12
newHash["ATEYA"] = 600
newHash["ATEYA"] = 60000
print(newHash.arr)
print(newHash["ATEYA"])
del newHash["ATEYA"]
print(newHash["ATEYA"])
