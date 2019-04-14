# -*- coding: utf-8 -*-
# Created on Sun Apr 14 2019 12:43:15
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# bottom-up dfs
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[2]
    
    def dfs(self, root):
        min_num, max_num, max_diff = root.val, root.val, 0
        if root.left:
            left = self.dfs(root.left)
            min_num = min(min_num, left[0])
            max_num = max(max_num, left[1])
            max_diff = max(max_diff, left[2])
        if root.right:
            right = self.dfs(root.right)
            min_num = min(min_num, right[0])
            max_num = max(max_num, right[1])
            max_diff = max(max_diff, right[2])
        max_diff = max([abs(max_num - root.val), abs(min_num - root.val), max_diff])
        return (min_num, max_num, max_diff)
