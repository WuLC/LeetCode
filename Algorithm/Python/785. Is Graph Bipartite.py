# -*- coding: utf-8 -*-
# Created on Mon Mar 19 2018 22:47:8
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bfs, use two types of colors to color the nodes
# pay attention that there may be multiple distinct parts in the graph
from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [0 for _ in xrange(n)]
        for i in xrange(n):
            if color[i] == 0:
                color[i] = 1
                queue = deque([i])
                while len(queue) > 0:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if color[neighbor] == 0:
                            color[neighbor] = 1 if color[curr] == 2 else 2
                            queue.append(neighbor)
                        elif color[neighbor] == color[curr]:
                            return False
        return True