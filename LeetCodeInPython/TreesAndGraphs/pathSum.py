"""
    #112 easy
    Given a binary tree and some target, find if a root to leaf path exist where summation of all elements on the path equals target.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None 

class Solution:

    def hasSum(self, root:TreeNode, target_sum : int, curr_sum)->bool:
        if (not root):
            return False

        curr_sum += root.val
        if (curr_sum == target_sum and root.left is None and root.right is None):
            return True 

        return self.hasSumr(root.left, target_sum, curr_sum) or self.hasSumr(root.right, target_sum, curr_sum)


    def hasPathSum(self, root_node:TreeNode, target_sum:int) ->bool:
        return self.hasSum(root_node, target_sum, 0)

