# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-07-09 09:40:53
# @Last Modified by:   WuLC
# @Last Modified time: 2017-07-09 09:41:08


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# traverse level by level
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        values = []
        curr = [root]
        while len(curr) > 0:
            next = []
            count = 0
            for node in curr:
                count += node.val
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            values.append(1.0*count/len(curr))
            curr = next
        return values
        