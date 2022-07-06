
class Heap:
    def __init__(self, size):
        self.customList = (size + 1)*[None]
        self.heap_size = 0
        self.max_size = size + 1


def peekOfHeap(rootNode):
    """"Returns the first element in the heap"""
    if not rootNode:
        return
    return rootNode.customList[1]


def sizeOfHeap(rootNode):
    """Returns the size of Binary Heap"""
    if not rootNode:
        return 
    return rootNode.heap_size

newHeap = Heap(5)
print(sizeOfHeap(newHeap))