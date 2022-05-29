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
        if not root:
            return 0
        return self.helper(root.left, True) + self.helper(root.right, False)
    
    def helper(self, node, is_left):
        if not node:
            return 0
        if not node.left and not node.right and is_left:
            return node.val
        return self.helper(node.left, True) + self.helper(node.right, False)
        
# @lc code=end

