# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-03 11:37:50
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-03 11:39:15
# @Email: liangchaowu5@gmail.com


# dfs
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])
        self.dfs(board, click[0], click[1], m, n)
        return board
    
    def dfs(self, board, row, col, m, n):
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return
        
        next_positions = []
        count = 0
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                next_row, next_col = row+r, col+c
                if 0 <= next_row < m and 0 <= next_col < n and (next_row != row or next_col != col) :
                    if board[next_row][next_col] == 'M':
                        count += 1
                    elif board[next_row][next_col] == 'E':
                        next_positions.append([next_row, next_col])
        if count != 0:
            board[row][col] = str(count)
            return 
        else:
            board[row][col] = 'B'
            for pos in next_positions:
                self.dfs(board, pos[0], pos[1], m, n)


// 