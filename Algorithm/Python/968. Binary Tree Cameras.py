# -*- coding: utf-8 -*-
# Created on Sat Jan 12 2019 14:7:7
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# greedy dfs, each node has three states
# 0 means that the node has been monitored but has no camera on it
# 1 means that the node has been monitored and has camera on it
# 2 means that the node has not been monitored
# referer: https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC++Python-Greedy-DFS

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        if self.dfs(root) == 2:
            self.result += 1
        return self.result
    
    def dfs(self, root):
        if root == None:
            return 0
        left, right = self.dfs(root.left), self.dfs(root.right)
        if left == 2 or right == 2:
            self.result += 1
            return 1
        return 2 if left == 0 and right == 0 else 0
        