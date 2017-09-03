# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-03 10:29:16
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-03 10:29:32

# recursive

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if L <= root.val <= R:
            left = self.trimBST(root.left, L, R)
            right = self.trimBST(root.right, L, R)
            root.left = left
            root.right = right
            return root
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            return self.trimBST(root.left, L, R)
        
