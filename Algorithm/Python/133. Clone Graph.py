# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-21 10:25:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-21 10:26:16
# @Email: liangchaowu5@gmail.com

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


# hash table and BFS
# O(n) time complexity, O(n) space, AC
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None:
            return None
        visited = set()
        que = collections.deque()
        nodes = {}
        que.append(node)
        visited.add(node)
        idx = 0
        while idx != len(que):
            curr = que[idx]
            idx += 1
            nodes[curr] = UndirectedGraphNode(curr.label)
            for node in curr.neighbors:
                if node not in visited:
                    visited.add(node)
                    que.append(node)
        start_node = None
        for node in que:
            curr = nodes[node]
            for neighbor in node.neighbors:
                curr.neighbors.append(nodes[neighbor])
            if start_node == None:
                start_node = curr
        return start_node
                
            
            
        