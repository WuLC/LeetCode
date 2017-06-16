# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-16 09:34:18
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-16 09:49:50
# @Email: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None and s == None:
            return True
        if t == None or s == None:
            return False
        if s.val == t.val and self.rootSubtree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def rootSubtree(self, s, t):
        if t == None and s == None:
            return True
        if t == None or s == None or s.val != t.val:
            return False
        return self.rootSubtree(s.left, t.left) and self.rootSubtree(s.right, t.right)


# same as above, but more graceful
class Solution(object):
    def isSubtree(self, s, t):
        if s == None:
            return False
        if self.isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    
    def isSame(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)