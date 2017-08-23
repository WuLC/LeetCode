# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-08-23 21:14:55
# @Last Modified by:   LC
# @Last Modified time: 2017-08-23 21:44:59

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# level traversal
# store the node and its index
# for a node with index i, the index of its left child i*2, the index of its right child is i * 2 + 1
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        result = 0
        curr, next = [(1, root)], []
        while len(curr) > 0:
            result = max(result, curr[-1][0] - curr[0][0] + 1)
            for index, node in curr:
                if node.left:
                    next.append((index * 2, node.left))
                if node.right:
                    next.append((index * 2 + 1, node.right))
            curr, next = next, []
        return result
            