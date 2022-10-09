#
# @lc app=leetcode id=129 lang=python
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# two types of backtracking
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result, self.candidate = 0, [str(root.val)]
        self.dfs(root)
        return self.result
    

    def dfs(self, node):
        if node == None:
            return
        if node.left == None and node.right == None:
            self.result += int(''.join(self.candidate))
            return
        for child in (node.left, node.right):
            if child:
                self.candidate.append(str(child.val))
                self.dfs(child)
                self.candidate.pop()

        
class Solution1(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result, self.candidate = 0, []
        self.dfs(root)
        return self.result
    

    def dfs(self, node):
        if node == None:
            return
        self.candidate.append(str(node.val))
        if node.left == None and node.right == None:
            self.result += int(''.join(self.candidate))
        else:
            self.dfs(node.left)
            self.dfs(node.right)
        self.candidate.pop()
# @lc code=end

