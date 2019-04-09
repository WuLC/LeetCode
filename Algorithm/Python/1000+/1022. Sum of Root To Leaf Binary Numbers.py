# -*- coding: utf-8 -*-
# Created on Mon Apr 08 2019 22:49:24
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)
    
    def dfs(self, root, curr):
        if root.left == None and root.right == None:
            return curr * 2 + root.val
        tmp = 0
        if root.left:
            tmp += self.dfs(root.left, curr * 2 + root.val)
        if root.right:
            tmp += self.dfs(root.right, curr * 2 + root.val)
        return tmp