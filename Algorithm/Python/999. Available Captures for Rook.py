# -*- coding: utf-8 -*-
# Created on Thu Feb 28 2019 9:8:56
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in xrange(8):
            for j in xrange(8):
                if board[i][j] == 'R':
                    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
                    for d in directions:
                        ni, nj = i, j
                        while 0 <= ni+d[0] < 8 and 0 <= nj+d[1] < 8:
                            ni += d[0]
                            nj += d[1]
                            if board[ni][nj] == 'B':
                                break
                            elif board[ni][nj] == 'p':
                                result += 1
                                break
                    return result
        return result