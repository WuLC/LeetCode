# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-22 23:49:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-22 23:50:11
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None: return []
        self.helper([root], False, result)
        return result
        
    def helper(self, nodes, reverse, result):
        if len(nodes) == 0:
            return
        next_level, values = [], []
        for node in nodes:
            values.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if reverse:
            values.reverse()
            result.append(values)
            self.helper(next_level, False, result)
        else:
            result.append(values)
            self.helper(next_level, True, result)