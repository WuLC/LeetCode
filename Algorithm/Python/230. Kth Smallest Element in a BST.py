# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-24 15:23:25
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-24 15:27:20
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        curr, nodes, count = root, [], 0
        while curr or nodes:
            if curr:
                nodes.append(curr)
                curr = curr.left
            else:
                curr = nodes.pop()
                count += 1
                if count == k:
                    return curr.val
                curr = curr.right