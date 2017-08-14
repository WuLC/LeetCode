# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-14 16:43:00
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-14 16:43:47


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = self.getHeight(root)
        width = 2**height - 1
        self.result = [['' for j in xrange(width)] for i in xrange(height)]
        self.fill(root, 0, 0, width)
        return self.result
    

    def getHeight(self, root):
        if root == None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
        
    def fill(self, root, row, left, right):
        if root == None:
            return
        mid = left + ((right - left) >> 1)
        self.result[row][mid] = str(root.val)
        self.fill(root.left, row + 1, left, mid - 1)
        self.fill(root.right, row + 1, mid + 1, right)