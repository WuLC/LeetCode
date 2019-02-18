# -*- coding: utf-8 -*-
# Created on Mon Feb 18 2019 8:42:27
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# simple recursive
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root.val == x or root.val == y:
            return False
        record = {}
        self.dfs(root, x, y, 0, record)
        return record['x'][0] != record['y'][0] and record['x'][1] == record['y'][1]

    def dfs(self, root, x, y, depth, record):
        if len(record) == 2:
            return
        if root.left:
            if root.left.val == x:
                record['x'] = (root.val, depth+1)
            elif root.left.val == y:
                record['y'] = (root.val, depth+1)
            self.dfs(root.left, x, y, depth+1, record)
        if root.right:
            if root.right.val == x:
                record['x'] = (root.val, depth+1)
            elif root.right.val == y:
                record['y'] = (root.val, depth+1)
            self.dfs(root.right, x, y, depth+1, record)