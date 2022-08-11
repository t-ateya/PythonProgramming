"""
    #Medium 230
    Given a binary search tree, find the kth smallest element in it.

    Solution:
    Use inorder traversal : left, root, right
"""
class TreeNode:
    def __init__(self, x):
        self.left = None 
        self.right = None 
        self.value = x

class Solution:
    def kthSmallest(self, root:TreeNode, k:int)->int:
        self.k = k 
        self.res = None 

        self.inorder(root)

        return self.res

    def inorder(self, root:TreeNode):
        if not root:
            return 

        self.inorder(root.left)

        self.k -=1
        if self.k == 0:
            self.res = root.value
            return 
        
        self.inorder(root.right)

s = Solution()
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(7)

node1.left = node2 
node1.right = node3


s.kthSmallest(node1,1)