# -*- coding: utf-8 -*-
# Created on Mon Jul 23 2018 9:47:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# change direction with index
# store obstacles in a map
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obs_map = {}
        for x, y in obstacles:
            obs_map.setdefault(x, set())
            obs_map[x].add(y)
        
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        result = 0
        d = 0
        x, y = 0, 0
        for c in commands:
            if c == -1:
                d += 1
                d = (d+4) % 4
            elif c == -2:
                d -= 1
                d = (d+4) % 4
            else:
                step = 0
                while step < c and not (x+dirs[d][0] in obs_map and y+dirs[d][1] in obs_map[x+dirs[d][0]]):
                    x += dirs[d][0]
                    y += dirs[d][1]
                    step += 1
            result = max(result, x**2 + y**2)
        return result