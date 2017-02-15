# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-15 19:51:22
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-15 19:52:28
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# traverse the tree row by row and get the value of the first node of the row each time 
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = root.val
        curr_row = [root]
        while curr_row:
            next_row = []
            for node in curr_row:
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            result = curr_row[0].val
            curr_row = next_row
        return result