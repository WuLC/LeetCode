# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-08-07 10:23:32
# @Last modified by:   LC
# @Last Modified time: 2017-08-07 10:30:50
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# format the tree as a list
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = self.format(root)
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            if nums[p1] + nums[p2] == k:
                return True
            elif nums[p1] + nums[p2] > k:
                p2 -= 1
            else:
                p1 += 1
        return False
    
    
    def format(self, root):
        if root == None:
            return []
        return self.format(root.left) + [root.val] + self.format(root.right)