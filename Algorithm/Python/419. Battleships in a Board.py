# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-24 16:58:53
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-24 16:59:23
# @Email: liangchaowu5@gmail.com

# the given board is already valid
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        if m==0:
            return 0
        n = len(board[0])
        count = 0
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == '.' or (j>0 and board[i][j-1] == 'X') or (i>0 and board[i-1][j] == 'X'):
                    continue
                count += 1
        return count
        