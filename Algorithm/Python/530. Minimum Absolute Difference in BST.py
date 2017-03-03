# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-03 12:05:28
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-03 12:22:25
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




# minimum value of any tow connected nodes
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val = None
        for sub_tree in [root.left, root.right]:
            if sub_tree:
                min_val = abs(root.val - sub_tree.val) if min_val == None else min(min_val, abs(root.val - sub_tree.val))
                sub_min = self.getMinimumDifference(sub_tree)
                if sub_min: 
                    min_val = min(min_val, sub_min)
        return min_val
            

# minimum value of any two nodes 
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_diff = None
        left_max, right_min = None, None
        if root.left:
            left_max = root.left
            while left_max.right:
                left_max = left_max.right
        if root.right:
            right_min = root.right
            while right_min.left:
                right_min = right_min.left
        if left_max:
            min_diff = abs(root.val - left_max.val)
        if right_min:
            min_diff = abs(root.val - right_min.val) if min_diff == None else min(abs(root.val - right_min.val), min_diff)
        
        for sub in [root.left, root.right]:
            if sub:
                sub_min = self.getMinimumDifference(sub)
                if sub_min and sub_min < min_diff:
                    min_diff = sub_min
        return min_diff