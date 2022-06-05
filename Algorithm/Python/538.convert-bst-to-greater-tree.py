#
# @lc app=leetcode id=538 lang=python
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.curr_sum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """        
        self.curr_sum = 0
        self.dfs(root)
        return root
    
    def dfs(self, root):
        if root == None:
            return
        self.dfs(root.right)
        self.curr_sum += root.val
        root.val = self.curr_sum
        self.dfs(root.left)
 
# @lc code=end

