#
# @lc app=leetcode id=404 lang=python
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root.left, True)
        self.dfs(root.right, False)
        return self.result
    
    def dfs(self, node, is_left):
        if node is None:
            return 
        if is_left and node.left == None and node.right == None:
            self.result += node.val
            return 
        self.dfs(node.left, True)
        self.dfs(node.right, False)
        
# @lc code=end

