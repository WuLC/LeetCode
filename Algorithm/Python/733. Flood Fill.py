# -*- coding: utf-8 -*-
# Created on Sun Nov 26 2017 11:43:38
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# dfs, O(1) space, change the value to -1 to represent visited
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        R, C = len(image), len(image[0])
        self.dfs(image, sr, sc, R, C, image[sr][sc])
        image[sr][sc] = -1
        for i in xrange(R):
            for j in xrange(C):
                if image[i][j] == -1:
                    image[i][j] = newColor
        return image
    
    def dfs(self, image, r, c, R, C, val):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for d in directions:
            if 0<=r+d[0]<R and 0<=c+d[1]<C and image[r+d[0]][c+d[1]] == val:
                image[r+d[0]][c+d[1]] = -1
                self.dfs(image, r+d[0], c+d[1], R, C, val)