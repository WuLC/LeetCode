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
        result = []
        self.dfs(result, [], root, targetSum)
        return result
    
    def dfs(self, result, tmp, node, target):
        if node == None:
            return
        if node.left == None and node.right == None and target == node.val:
            tmp.append(node.val)
            result.append(tmp)
        for _node in [node.left, node.right]:
            if _node != None:
                self.dfs(result, tmp + [node.val], _node, target - node.val)

        
# @lc code=end

