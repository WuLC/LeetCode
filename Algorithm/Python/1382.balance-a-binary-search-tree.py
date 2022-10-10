#
# @lc app=leetcode id=1382 lang=python
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nums = []
        self.traverse(root, nums)
        return self.construct(nums, 0, len(nums) - 1)
    
    def traverse(self, node, nums):
        if node == None:
            return
        self.traverse(node.left, nums)
        nums.append(node.val)
        self.traverse(node.right, nums)
    
    def construct(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        mid = start + ((end - start)>>1)
        root = TreeNode(nums[mid])
        root.left = self.construct(nums, start, mid-1)
        root.right = self.construct(nums, mid+1, end)
        return root


        
# @lc code=end

