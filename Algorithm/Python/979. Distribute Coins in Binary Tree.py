# -*- coding: utf-8 -*-
# Created on Sun Jan 20 2019 11:22:18
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recurvsive with postorder traverse
# refer: https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.traverse(root)
        return self.result
    
    def traverse(self, root):
        if root == None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.result += abs(left) + abs(right)
        return root.val + left + right - 1