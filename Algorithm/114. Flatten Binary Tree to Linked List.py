# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-08 19:38:01
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-08 19:38:13
# @Email: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack, nodes = [], []
        curr_node = root
        while len(stack) != 0 or curr_node != None:
            if curr_node != None:
                stack.append(curr_node)
                nodes.append(curr_node)
                curr_node = curr_node.left
            else:
                tmp = stack.pop()
                curr_node = tmp.right
        for i in xrange(len(nodes)-1):
            nodes[i].left, nodes[i].right = None, nodes[i+1]