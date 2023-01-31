class MyList:
    def __init__(self, length):
        self._length = length
    @property
    def length(self):
        return self._length

    def __len__(self):
        print("__len__ called")
        return self.length

    def __bool__(self):
        print("__bool__ called__")
        return self.length > 0

l1 = MyList(0)    
l2 = MyList(10)    

print(bool(l1))
print(bool(l2))

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __bool__(self):
        return self.x !=0 or self.y != 0

    