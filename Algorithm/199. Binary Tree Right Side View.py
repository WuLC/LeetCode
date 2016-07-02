# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-02 09:35:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-02 09:36:03
# @Email: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        nodes, result = [root], []
        while nodes:
            tmp, next_level = [], []
            for node in nodes:
                tmp.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            result.append(tmp[-1])
            nodes = next_level
        return result
                