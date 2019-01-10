# -*- coding: utf-8 -*-
# Created on Thu Jan 10 2019 22:36:20
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        if root == None and len(voyage) == 0:
            return []
        elif (root == None and len(voyage) > 0) or (root != None and len(voyage) == 0) or (root.val != voyage[0]):
            return [-1]
        result = []
        left_idx, right_idx = len(voyage) , len(voyage)
        for i in xrange(1, len(voyage)):
            if root.left and voyage[i] == root.left.val:
                left_idx = i
            if root.right and voyage[i] == root.right.val:
                right_idx = i

        if left_idx == 1:
            tmp = self.flipMatchVoyage(root.left, voyage[left_idx : right_idx])
            if right_idx != len(voyage):
                tmp += self.flipMatchVoyage(root.right, voyage[right_idx:])
        elif right_idx == 1:
            tmp = self.flipMatchVoyage(root.right, voyage[right_idx : left_idx])
            if left_idx != len(voyage):
                result.append(root.val)
                tmp += self.flipMatchVoyage(root.left, voyage[left_idx:])
        else:
            return [-1]
        
        for num in tmp:
            if num != -1:
                result.append(num)
            else:
                return [-1]
        return result