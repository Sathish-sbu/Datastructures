"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val = root.val
        return (self.check(root.left, val) and self.check(root.right, val))
    
    def check(self, node, val):
        if node == None:
            return True
        else :
            return node.val == val and self.check(node.left, val) and self.check                   (node.right, val)
    
