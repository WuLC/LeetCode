# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-11 11:27:19
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-11 11:27:28
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0: return []  # without this ,the result will be [[]],which is not equal to the result []
        return self.helper(1, n)
    
    def helper(self,begin,end):
        if begin > end:
            return [None]
        if begin == end:
            return [TreeNode(begin)]
        result = []
        for i in xrange(begin,end+1):
            tmp = []
            left = self.helper(begin, i-1)
            right = self.helper(i+1, end)
            for m in left:
                for n in right:
                    root = TreeNode(i)
                    root.left, root.right = m, n
                    result.append(root)
        return result
            
            
        