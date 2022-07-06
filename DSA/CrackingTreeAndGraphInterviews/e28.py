"""
    First common ancestor - LeetCode 236
    Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in 
    a data structure. NOTE: This is not necessary a binary search tree
"""

def find_node_in_tree(target, root_node):
    if not root_node:
        return False
    if target == root_node:
        return True 
    else:
        return (find_node_in_tree(target, root_node.left) or find_node_in_tree(target, root_node.right))

def find_first_common_ancestor(node1, node2, root_node):
    """This function returns the first common ancestor of two given nodes in a binary tree"""
    n1OnLeft = find_node_in_tree(node1, root_node.left)
    n2OnLeft = find_node_in_tree(node2, root_node.left)

    if n1OnLeft ^ n2OnLeft:  #n1OnLeft XOR n2OnLeft
        return root_node
    else:
        if n1OnLeft:
            return find_first_common_ancestor(node1, node2, root_node.left)
        else:
            return find_first_common_ancestor(node1, node2, root_node.right)


class Node:
    def __init__(self, value, left=None, right = None):
        self.value = value 
        self.left = left 
        self.right = right

node54 = Node(54)
node88 = Node(88, node54)
node35 = Node(35)
node22 = Node(22, node35, node88)
node33 = Node(33)
node90  = Node(90,right=node33)
node95 = Node(95)
node99 = Node(99, node90, node95)
node44 = Node(44, node22, node99)
node77 = Node(77)
root_node = Node(55, node44, node77)     

common_ancestor = find_first_common_ancestor(node44,node77, root_node)
print(common_ancestor.value)
    
