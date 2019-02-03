# -*- coding: utf-8 -*-
# Created on Sun Feb 03 2019 18:3:18
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
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        left, right = self.smallestFromLeaf(root.left), self.smallestFromLeaf(root.right)
        if len(left) == 0:
            return right + chr(root.val + 97)
        elif len(right) == 0:
            return left + chr(root.val + 97)
        else:
            return min(left, right) + chr(root.val + 97)