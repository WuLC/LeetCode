# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-18 20:25:17
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-18 20:26:42
# @Email: liangchaowu5@gmail.com

# method 1,bracking,AC
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        if len(board) == 0:
            return False
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if self.helper(board,word,i,j,m,n):
                    return True
        return False
    
    def helper(self,board,word,i,j,m,n):
        if len(word) == 0:
            return True
        if i<0 or i>=m or j<0 or j>=n or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '.'
        if self.helper(board,word[1:],i-1,j,m,n) or\
        self.helper(board,word[1:],i+1,j,m,n) or\
        self.helper(board,word[1:],i,j-1,m,n) or\
        self.helper(board,word[1:],i,j+1,m,n):
            return True
        else:
            board[i][j] = tmp



# method 2,backtracking,TLE for some cases
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        if len(board) == 0:
            return False
        m = len(board)
        n = len(board[0])
        candidate = []
        used = set()
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    candidate.append((i,j))
        if self.helper(board,word,0,candidate,used):
            return True
        else:
            return False

                   
    def helper(self,board,word,k,candidate,used):
        if k+1 == len(word):
            return True
        m = len(board)
        n = len(board[0])
        sub = []
        for c in candidate:
            if c not in used:
                i,j=c
                if i-1 >= 0 and board[i-1][j] == word[k+1] and (i-1,j) not in used:
                    sub.append((i-1,j))
                if i+1<m and board[i+1][j] == word[k+1] and (i+1,j) not in used:
                    sub.append((i+1,j))
                if j-1>=0 and board[i][j-1] == word[k+1] and (i,j-1) not in used:
                    sub.append((i,j-1))
                if j+1<n and board[i][j+1] == word[k+1] and (i,j+1) not in used:
                    sub.append((i,j+1))
                if len(sub)>0:
                    used.add(c)
                    if self.helper(board,word,k+1,sub,used):
                        return True
                    else:
                        used.remove(c)
        return False   