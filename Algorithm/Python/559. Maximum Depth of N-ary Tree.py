# -*- coding: utf-8 -*-
# Created on Fri Jul 27 2018 19:10:19
# Author: WuLC
# EMail: liangchaowu5@gmail.com

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# recursive
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        if len(root.children) == 0:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)