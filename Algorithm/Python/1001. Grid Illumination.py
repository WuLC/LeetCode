# -*- coding: utf-8 -*-
# Created on Wed Feb 27 2019 8:40:28
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# record the number of lights at each row, column, left diagonal and right diagonal
# use hashmap instead of list to avoid memory limit exceeded

from collections import defaultdict

class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        row, col = defaultdict(int), defaultdict(int)
        left_diagonal, right_diagonal = defaultdict(int), defaultdict(int)
        source = defaultdict(set)
        for i, j in lamps:
            source[i].add(j)
            row[i] += 1
            col[j] += 1
            left_diagonal[i+j] += 1
            right_diagonal[i-j] += 1

        result = []
        for i, j in queries:
            if row[i] > 0 or col[j] > 0 or left_diagonal[i+j] > 0 or right_diagonal[i-j] > 0:
                result.append(1)
            else:
                result.append(0)
            for r in [i-1, i+2]:
                for c in [j-1, j+2]:
                    if c in source[r]:
                        row[r] -= 1
                        col[c] -= 1
                        left_diagonal[r+c] -= 1
                        right_diagonal[r-c] -= 1
        return result
