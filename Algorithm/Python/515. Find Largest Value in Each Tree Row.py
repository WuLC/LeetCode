# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-15 19:41:32
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-15 19:42:09
# @Email: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# traverse the tree row by row and find the max value in each row
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None: return result
        curr_row = [root]
        while curr_row:
            next_row = []
            curr_max = None
            for node in curr_row:
                curr_max = node.val if curr_max == None else max(curr_max, node.val)
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            result.append(curr_max)
            curr_row = next_row
        return result