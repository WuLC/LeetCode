# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-04 20:38:37
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-04 21:01:37
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 1, TLE, O(n^2)
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: 
            return 0
        tmp, left, right = root.val, self.helper(root.left), self.helper(root.right)    
        if left > 0: tmp += left 
        if right > 0: tmp += right 
        left_sum, right_sum = None, None
        if root.left: left_sum = self.maxPathSum(root.left)
        if root.right: right_sum = self.maxPathSum(root.right)
        return max(tmp, left_sum, right_sum)
    
    # helper(node) represents the maximal sum that the path can get with node as root
    def helper(self, root):
        if root == None:
            return 0
        tmp = max(self.helper(root.left),self.helper(root.right))
        if tmp>0:
            return root.val + tmp
        else:
            return root.val



# method 2, AC, O(n)
# improvement on based on method 1, as the maximal path will take one node of the tree as root, thus one traversal is enough
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        result = [root.val]
        self.helper(root, result)
        return result[0]
    
    
    def helper(self, root, result):
        if root == None:
            return 0
        left = max(0, self.helper(root.left, result))
        right = max(0, self.helper(root.right, result))
        result[0] = max(result[0], left + right + root.val)
        return max(left, right)+root.val