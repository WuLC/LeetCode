# -*- coding: utf-8 -*-
# Created on Sun Jun 09 2019 18:3:37
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# recursive solution 1
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        if root.left == None and root.right == None:
            return None if root.val < limit else root
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None


# recursive solution 2, why not working?
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        self.dfs(root, 0, limit)
        return root if root.left or root.right else None

    def dfs(self, root, curr_sum, limit):
        curr_sum += root.val
        if root.left == None and root.right == None:
            return curr_sum < limit
        left_insuff = self.dfs(root.left, curr_sum, limit) if root.left != None else True
        right_insuff = self.dfs(root.right, curr_sum, limit) if root.right != None else True
        if left_insuff:
            root.left = None
        if right_insuff:
            root.right = None
        return left_insuff and right_insuff