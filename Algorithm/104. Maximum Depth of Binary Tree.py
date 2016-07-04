# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-04 15:52:09
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-04 15:52:20
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        nodes, count = [root], 0
        while nodes:
            next_level = []
            for node in nodes:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            count += 1
            nodes = next_level
        return count