# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-09 08:30:49
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-09 09:31:05
# @Email: liangchaowu5@gmail.com

# method 1,DFS,  stack overflow
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        visited = [[0 for j in xrange(n)] for i in xrange(m)]
        
        # traverse the edges of the board
        for j in xrange(n):
            if board[i][j] == 'O' and visited[i][j] == 0:
                self.dfs(i, j, m, n, visited, board)
    
        for i in xrange(m):
            if board[i][j] == 'O' and visited[i][j] == 0:
                self.dfs(i, j, m, n, visited, board)

        for i in xrange(1, m-1):
            for j in xrange(1, n-1):
                if visited[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
    
    def dfs(self, row, col, m, n, visited, board):
        visited[row][col] = 1
        if row-1>=0 and visited[row-1][col] == 0 and board[row-1][col] == 'O':
            self.dfs(row-1, col, m, n, visited, board)
        if row+1 < m and visited[row+1][col] == 0 and board[row+1][col] == 'O':
            self.dfs(row+1, col, m, n, visited, board)
        if col-1>=0 and visited[row][col-1] == 0 and board[row][col-1] == 'O':
            self.dfs(row, col-1, m, n, visited, board)
        if col+1<n and visited[row][col+1] == 0 and board[row][col+1] == 'O':
            self.dfs(row, col+1, m, n, visited, board)


# method 2 ,base on method 1 
# just imply small improvement on function dfs, that is don't dfs the edges
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        visited = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in [0, m-1]:
            for j in xrange(n):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    self.dfs(i, j, m, n, visited, board)
        for j in [0, n-1]:
            for i in xrange(m):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    self.dfs(i, j, m, n, visited, board)
        for i in xrange(1, m-1):
            for j in xrange(1, n-1):
                if visited[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
    
    def dfs(self, row, col, m, n, visited, board):
        visited[row][col] = 1
        if row>1 and visited[row-1][col] == 0 and board[row-1][col] == 'O':
            self.dfs(row-1, col, m, n, visited, board)
        if row<m-2 and visited[row+1][col] == 0 and board[row+1][col] == 'O':
            self.dfs(row+1, col, m, n, visited, board)
        if col>1 and visited[row][col-1] == 0 and board[row][col-1] == 'O':
            self.dfs(row, col-1, m, n, visited, board)
        if col<n-2 and visited[row][col+1] == 0 and board[row][col+1] == 'O':
            self.dfs(row, col+1, m, n, visited, board)


# method 3, DFS, base on method 2, use constant space instead of O(m*n) space in method 2
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        for i in [0, m-1]:
            for j in xrange(n):
                if board[i][j] == 'O':
                    self.dfs(i, j, m, n, board)
        for j in [0, n-1]:
            for i in xrange(m):
                if board[i][j] == 'O':
                    self.dfs(i, j, m, n, board)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    
    def dfs(self, row, col, m, n, board):
        board[row][col] = '#'
        if row>1 and board[row-1][col] == 'O':
            self.dfs(row-1, col, m, n, board)
        if row<m-2  and board[row+1][col] == 'O':
            self.dfs(row+1, col, m, n, board)
        if col>1  and board[row][col-1] == 'O':
            self.dfs(row, col-1, m, n, board)
        if col<n-2  and board[row][col+1] == 'O':
            self.dfs(row, col+1, m, n, board)


# method 4, BFS, slower than DFS
from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        for i in [0, m-1]:
            for j in xrange(n):
                if board[i][j] == 'O':
                    self.bfs(i, j, m, n, board)
        for j in [0, n-1]:
            for i in xrange(m):
                if board[i][j] == 'O':
                    self.bfs(i, j, m, n, board)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    
    def bfs(self, row, col, m, n, board):
        que = deque()
        que.append((row,col))
        board[row][col] = '#'
        while que:
            row, col = que.popleft()
            if row>1 and board[row-1][col] == 'O':
                que.append((row-1, col))
                board[row-1][col] = '#'
            if row<m-2  and board[row+1][col] == 'O':
                que.append((row+1, col))
                board[row+1][col] = '#'
            if col>1 and board[row][col-1] == 'O':
                que.append((row, col-1))
                board[row][col-1] = '#'
            if col<n-2 and board[row][col+1] == 'O':
                que.append((row, col+1))
                board[row][col+1] = '#'