# -*- coding: utf-8 -*-
# Created on Sun Dec 17 2017 13:39:9
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashmap
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 2 or len(grid[0]) < 0:
            return 0
        result = 0
        count = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count.setdefault(i, set())
                    count[i].add(j)
        t = list(count.values())
        for i in range(len(t)):
            for j in range(i+1, len(t)):
                n = len(t[i]&t[j])
                result += (n*(n-1))/2
        return result