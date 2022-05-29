#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result, tmp = [], []
        if root == None:
            return result
        self.dfs(result, tmp, root)
        return result

    def dfs(self, result, tmp, node):
        tmp.append(str(node.val))
        if node.left == None and node.right == None:
            result.append("->".join(tmp))
        else:
            for _node in [node.left, node.right]:
                if _node != None:
                    self.dfs(result, tmp, _node)
        tmp.pop()
# @lc code=end

