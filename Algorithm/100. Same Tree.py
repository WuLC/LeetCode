# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-13 23:41:42
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-14 11:45:42
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None: return q==None
        if q == None: return p==None
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)