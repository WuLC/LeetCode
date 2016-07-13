# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-13 14:56:28
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-13 14:56:35
# @Email: liangchaowu5@gmail.com

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return
        nodes = [root]
        while nodes:
            next_level = []
            for i in xrange(len(nodes)):
                if nodes[i].left:
                    next_level.append(nodes[i].left)
                if nodes[i].right:
                    next_level.append(nodes[i].right)
                if i != len(nodes)-1:
                    nodes[i].next = nodes[i+1]
            nodes = next_level