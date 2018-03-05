# -*- coding: utf-8 -*-
# Created on Mon Feb 12 2018 20:40:31
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
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tmp = []
        if root.left:
            curr = root.left
            while curr.right:
                curr = curr.right
            tmp.append(root.val - curr.val)
            if root.left.left or root.left.right:
                tmp.append(self.minDiffInBST(root.left))
        if root.right:
            curr = root.right
            while curr.left:
                curr = curr.left
            tmp.append(curr.val - root.val)
            if root.right.left or root.right.right:
                tmp.append(self.minDiffInBST(root.right))
        return min(tmp)
                
        