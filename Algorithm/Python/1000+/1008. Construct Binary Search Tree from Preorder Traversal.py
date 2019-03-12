# -*- coding: utf-8 -*-
# Created on Mon Mar 11 2019 22:3:4
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(preorder, 0, len(preorder))

    def dfs(self, preorder, left, right):
        if left == right:
            return None
        root = TreeNode(preorder[left])
        r = left+1
        while r < len(preorder) and preorder[r] < preorder[left]:
            r += 1
        root.left = self.dfs(preorder, left+1, r)
        root.right = self.dfs(preorder, r, right)
        return root
