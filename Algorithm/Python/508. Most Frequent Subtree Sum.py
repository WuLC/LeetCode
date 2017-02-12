# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-13 00:11:34
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-13 00:11:50
# @Email: liangchaowu5@gmail.com



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive
# 
class Solution(object):
    def __init__(self):
        self.count = None
        
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.count = collections.defaultdict(int)
        if root==None: 
            return []
        self.count[self.helper(root)] += 1
        most_occur = max(self.count.values())
        return [k for k,v in self.count.items() if v == most_occur]
        
    def helper(self, curr):
        left_sum, right_sum = 0, 0
        if curr.left:
            left_sum = self.helper(curr.left)
            self.count[left_sum] += 1
        if curr.right:
            right_sum = self.helper(curr.right)
            self.count[right_sum] += 1
        return curr.val + left_sum + right_sum