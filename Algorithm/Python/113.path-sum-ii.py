#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result, candidate = [], []
        if root == None:
            return result

        # append root
        candidate.append(root.val)
        def dfs(node, target):
            if node.left == None and node.right == None and node.val == target:
                result.append(candidate[:])
                return
            for leaf in (node.left, node.right):
                if leaf:
                    candidate.append(leaf.val)
                    dfs(leaf, target - node.val)
                    candidate.pop()

        dfs(root, targetSum)
        return result
        
# @lc code=end

