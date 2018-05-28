# -*- coding: utf-8 -*-
# Created on Mon May 28 2018 19:6:28
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# simple bfs
from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        queue = deque([0])
        visited = set()
        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            for neighbor in rooms[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)
            visited.add(curr)
        return len(visited) == len(rooms)