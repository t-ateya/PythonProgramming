"""
    Problem Statement: List of Depths
        Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (i.e, if you 
        have a tree with depth D, you'll have D linked list)
"""

class LinkedList:
    def __init__(self, val):
        self.val = val 
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val = self.val) + str (self.next)


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 


def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1

    else:
        depth_left = 1 + depth(tree.left)
        depth_right = 1+ depth(tree.right)
        if depth_left > depth_right:
            return depth_left 
        else:
            return depth_right


def tree_to_linkedList(tree, custDict = {}, d = None):
    if d ==None:
        d = depth(tree)
    if custDict.get(d) == None:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
        
    if tree.left != None:
        custDict = tree_to_linkedList(tree.left, custDict, d-1)
    if tree.right != None:
        custDict = tree_to_linkedList(tree.right, custDict, d-1)
    return custDict


mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)

mainTree.left = two
mainTree.right = three

two.left = four 
two.right = five 

three.left = six 
three.right = seven

custDict = tree_to_linkedList(mainTree)

[print("{0} {1}".format(depth_level, linked_list)) for depth_level, linked_list in custDict.items()]