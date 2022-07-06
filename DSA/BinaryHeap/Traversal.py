
class Heap:
    def __init__(self, size):
        self.customArrayList = (size + 1)*[None]
        self.heap_size = 0
        self.max_size = size + 1


def peekOfHeap(rootNode):
    """"Returns the first element in the heap"""
    if not rootNode:
        return
    return rootNode.customArrayList[1]


def sizeOfHeap(rootNode):
    """Returns the size of Binary Heap"""
    if not rootNode:
        return 
    return rootNode.heap_size


def levelOrderTraversal(rootNode):
    """"Traverses the entire array in a level order and prints the value"""
    if not rootNode:
        return 
    else:
        for index in range(1, rootNode.heap_size + 1):
            print(rootNode.customArrayList[index])
        return 




newHeap = Heap(5)
print(sizeOfHeap(newHeap))