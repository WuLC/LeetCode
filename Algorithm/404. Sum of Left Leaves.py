# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-26 10:59:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-26 10:59:06
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if root == None else self.helper(root.left, left = True) + self.helper(root.right, left = False)
        
    
    def helper(self, root, left):
        if root == None:
            return 0
        if left and root and root.left == None and root.right == None:
            return root.val
        else:
            return self.helper(root.left, left = True) + self.helper(root.right, left = False)