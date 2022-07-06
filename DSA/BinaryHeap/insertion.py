
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


def heapifyTreeInsert(rootNode, childIndex, heapType):
    if childIndex <= 1:
        return
    parentIndex = int(childIndex/2) 

    if heapType.title() == "Min":
        #Check if parent is greater than childNode swap
        if rootNode.customArrayList[childIndex] < rootNode.customArrayList[parentIndex]:
            temp = rootNode.customArrayList[childIndex]
            rootNode.customArrayList[childIndex] = rootNode.customArrayList[parentIndex]
            rootNode.customArrayList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType.title() == "Max":
        if rootNode.customArrayList[childIndex] > rootNode.customArrayList[parentIndex]:
            temp = rootNode.customArrayList[childIndex]
            rootNode.customArrayList[childIndex] = rootNode.customArrayList[parentIndex]
            rootNode.customArrayList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType):
    if not rootNode:
        return 
    if rootNode.heap_size + 1 == rootNode.max_size:
        return "The BH is Full"
    else:
        rootNode.heap_size += 1
        rootNode.customArrayList[rootNode.heap_size] = nodeValue
        heapifyTreeInsert(rootNode, rootNode.heap_size, heapType)
        return "The value has been successfully inserted"

        


newHeap = Heap(5)
"""
insertNode(newHeap, 4, "MAX")
insertNode(newHeap, 5, "MAX")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 1, "max")
"""

insertNode(newHeap, 4, "Min")
insertNode(newHeap, 5, "Min")
insertNode(newHeap, 2, "Min")
insertNode(newHeap, 1, "min")

levelOrderTraversal(newHeap)
