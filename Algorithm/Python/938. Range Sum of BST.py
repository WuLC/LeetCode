# -*- coding: utf-8 -*-
# Created on Sun Nov 11 2018 10:58:0
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
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        range_sum = 0
        if root == None:
            return range_sum
        if root.val <= L:
            if root.val == L:
                range_sum += root.val
            range_sum += self.rangeSumBST(root.right, L, R)
        elif root.val >= R:
            if root.val == R:
                range_sum += root.val
            range_sum += self.rangeSumBST(root.left, L, R)
        else:
            range_sum += root.val
            range_sum += self.rangeSumBST(root.left, L, root.val) + self.rangeSumBST(root.right, root.val, R)
        return range_sum