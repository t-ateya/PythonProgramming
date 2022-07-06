
class Heap:
    def __init__(self, size):
        self.customList = (size + 1)*[None]
        self.heap_size = 0
        self.max_size = size + 1

newHeap = Heap(5)