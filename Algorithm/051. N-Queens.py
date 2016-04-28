# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-19 15:10:03
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-28 23:11:34
# @Email: liangchaowu5@gmail.com

# 方法一：回溯法
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        board = [['.' for i in range(n)] for j in range(n)] #生成n*n的原始矩阵
        self.helper(board, solutions,0 )
        return solutions
        
                
    def helper(self,board,solutions, row):
        n = len(board)
        if row==n:
            tmp=[]          
            for i in board:
                tmp.append(reduce(lambda x,y:x+y,i)) # reduce函数的作用是将['Q','.','.','.']转为'Q...'
            solutions.append(tmp)
            return
        
        for i in range(n):
            if self.is_valid(board,row,i):
                board[row][i] = 'Q'
                self.helper(board,solutions,row+1)
                board[row][i] = '.'


    def is_valid(self,board,i,j):
        n = len(board)
        # check column
        for k in xrange(n):
            if board[k][j] == 'Q':
                return False
        
        # check diagonal，只需要检查上面的两条边
        ri = i
        rj = j
        while 0<=i<=n-1 and 0<=j<=n-1:
            if board[i][j]=='Q':
                return False
            i-=1
            j-=1
        
        i = ri
        j = rj
        while 0<=i<=n-1 and 0<=j<=n-1:
            if board[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True

# 方法二：回溯法，与方法一不同点在于判断放入的皇后是否有效的方法不同
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        board = [['.' for i in range(n)] for j in range(n)] #生成n*n的原始矩阵
        col = [0 for i in range(n)]
        left_dia =  [0 for i in range(2*n-1)]
        right_dia = [0 for i in range(2*n-1)]

        self.helper(board, solutions,0, col,left_dia,right_dia)
        return solutions
        
                
    def helper(self,board,solutions,row,col,left_dia,right_dia):
        n = len(board)
        if row==n:
            tmp=[]          
            for i in board:
                tmp.append(reduce(lambda x,y:x+y,i)) # reduce函数的作用是将['Q','.','.','.']转为'Q...'
            solutions.append(tmp)
            return
        
        for i in range(n):
            if col[i]==0 and left_dia[row+i]==0 and right_dia[i-row+n-1]==0:
                board[row][i] = 'Q'
                col[i],left_dia[row+i],right_dia[i-row+n-1]=1,1,1
                self.helper(board,solutions,row+1,col,left_dia,right_dia)
                board[row][i] = '.'
                col[i],left_dia[row+i],right_dia[i-row+n-1]=0,0,0