# -*- coding: utf-8 -*-
# Created on Sun Aug 19 2018 12:28:44
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# construct graph from the original tree, then use bfs
from collections import defaultdict, deque
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = defaultdict(list)
        self.construct_graph(root, graph)
        # bfs
        result = []
        visited = set()
        original = target.val
        queue = deque([(original, 0)])
        while queue:
            val, dis = queue.popleft()
            if dis == K:
                result.append(val)
            visited.add(val)
            for neighbor in graph[val]:
                if neighbor not in visited:
                    queue.append((neighbor, dis+1))
        return result


    def construct_graph(self, root, graph):
        if root.left:
            graph[root.val].append(root.left.val)
            graph[root.left.val].append(root.val)
            self.construct_graph(root.left, graph)
        if root.right:
            graph[root.val].append(root.right.val)
            graph[root.right.val].append(root.val)
            self.construct_graph(root.right, graph)


        