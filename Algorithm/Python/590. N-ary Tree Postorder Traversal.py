# -*- coding: utf-8 -*-
# Created on Fri Jul 27 2018 19:17:58
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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        result = []
        for child in root.children:
            result.extend(self.postorder(child))
        result.append(root.val)
        return result