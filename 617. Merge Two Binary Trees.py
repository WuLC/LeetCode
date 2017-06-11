# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-06-11 11:31:01
# @Last modified by:   LC
# @Last Modified time: 2017-06-11 11:31:16
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def mergeTrees(self, r1, r2):
        """
        :type r1: TreeNode
        :type r2: TreeNode
        :rtype: TreeNode
        """
        if r1 == None and r2 == None:
            return None
        elif r1 == None:
            return r2
        elif r2 == None:
            return r1
        else:
            root = TreeNode(r1.val + r2.val)
            root.left = self.mergeTrees(r1.left, r2.left)
            root.right = self.mergeTrees(r1.right, r2.right)
            return root
            
        