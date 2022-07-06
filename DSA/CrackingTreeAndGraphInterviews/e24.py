

"""
    Check Balanced-Leetcode 110
    Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be 
    a tree such that the heigts of the two subtrees of any nodes never differ by more than one

    Solution
    The binary tree is  balanced if:
        -The right subtree is balanced
        - The left subtree is balanced
        - The diff b/n the height the height of right subtree and left subtree is at most 1
"""

def isBalancedHelper(root):
    """This function returns the height of a tree. Returns -1 if the tree in unbalanced"""
    if not root:
        return 0

    left_height = isBalancedHelper(root.left_child)
    if left_height == -1:
        return -1
    right_height = isBalancedHelper(root.right_child)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1
    
    return max(left_height, right_height) + 1

def is_balanced(root):
    print("height: ", isBalancedHelper(root))
    return isBalancedHelper(root) > -1
    

class Node():
    def __init__(self, data, left_child=None, right_child=None):
        self.left_child = left_child
        self.right_child = right_child
        self.data = data 


N1 = Node("N1")
N2 = Node("N2")
N3 = Node("N3")
N4 = Node("N4")
N5 = Node("N5")
N6 = Node("N6")
N7 = Node("N7")

N1.left_child = N2
N1.right_child = N3

N2.left_child = N4
N2.right_child = N5

N3.right_child = N6
#N6.right_child = N7
#N3.left_child = N7

print(is_balanced(N1))


