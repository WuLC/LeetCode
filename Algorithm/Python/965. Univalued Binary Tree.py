# -*- coding: utf-8 -*-
# Created on Thu Jan 03 2019 9:24:48
# Author: WuLC
# EMail: liangchaowu5@gmail.com

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
        if root.left:
            same_left = root.val == root.left.val and self.isUnivalTree(root.left)
            if not same_left:
                return False
        if root.right:
            same_right = root.val == root.right.val and self.isUnivalTree(root.right)
            if not same_right:
                return False
        return True