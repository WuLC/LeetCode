# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-30 17:10:21
# @Last Modified by:   WuLC
# @Last Modified time: 2017-03-30 17:12:45

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# traverse the tree in the order of right->mid->left 
# and accumulate the value of all the traversed nodes as sum of additional sum of the current node
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        curr = root
        accumulated_sum = 0
        stack = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                curr.val += accumulated_sum
                accumulated_sum = curr.val
                curr = curr.left
        return root
        