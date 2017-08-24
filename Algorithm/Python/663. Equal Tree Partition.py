# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-08-24 22:54:21
# @Last Modified by:   LC
# @Last Modified time: 2017-08-24 22:55:35


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, 0)
        
    
    def helper(self, root, prevSum):
        if root == None:
            return False
        leftSum = self.treeSum(root.left)
        rightSum = self.treeSum(root.right)
        if root.left and leftSum == prevSum + root.val + rightSum:
            return True
        if root.right and rightSum == prevSum + root.val + leftSum:
            return True
        return self.helper(root.left, prevSum + root.val + rightSum) or self.helper(root.right, prevSum + root.val + leftSum)
    
    def treeSum(self, root):
        if root == None:
            return 0
        return root.val + self.treeSum(root.left) + self.treeSum(root.right)
        