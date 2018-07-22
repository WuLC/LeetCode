# -*- coding: utf-8 -*-
# Created on Sun Jul 22 2018 10:52:7
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leaf_values(root1) == self.leaf_values(root2)
    
    def leaf_values(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        return self.leaf_values(root.left) + self.leaf_values(root.right)
        
        
