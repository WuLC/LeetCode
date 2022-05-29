#
# @lc app=leetcode id=513 lang=python
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0 
        result = 0
        queue = deque([root])
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                if i == 0:
                    result = queue[0].val
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)                
                if node.right:
                    queue.append(node.right)
        return result
                     
# @lc code=end

