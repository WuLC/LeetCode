# -*- coding: utf-8 -*-
# Created on Tue Feb 26 2019 21:5:55
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive, always insert to the right subtree of the current root
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None or val > root.val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root