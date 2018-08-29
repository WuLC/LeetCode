# -*- coding: utf-8 -*-
# Created on Wed Aug 29 2018 15:1:29
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
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N==0:
            return [None]
        if N==1:
            return [TreeNode(0)]
        result = []
        for i in xrange(1, N-1, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-1-i)
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left, root.right = l, r
                    result.append(root)
        return result