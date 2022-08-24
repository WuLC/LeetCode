#
# @lc app=leetcode id=968 lang=python
#
# [968] Binary Tree Cameras
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

    # # same idea as 337, but only pass some cases 
    # def dfs(self, node):
    #     if node is None:
    #         return (1, 1, 0) # not so resonable
    #     left = self.dfs(node.left)
    #     right = self.dfs(node.right)
    #     return (1 + min(left) + min(right),
    #             min(left[0] + min(right[0:2]), right[0] + min(left[0:2])),
    #             min(left[1:3]) + min(right[1:3])
    #         )
        if self.dfs(root) == 0:
            self.result += 1
        return self.result
        
        
    def dfs(self, node):
        """three states:
        0: not cover
        1: has camera
        2: has no camera but is covered
        """
        if not node:
            return 2
        left, right = self.dfs(node.left), self.dfs(node.right)
        if left == 0 or right == 0:
            self.result += 1
            return 1
        if left == 2 and right == 2:
            return 0
        if left == 1 or right == 1:
            return 2
        

# @lc code=end

