# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-09 09:57:54
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:22:11
# @Email: liangchaowu5@gmail.com


# 思路：字典存储行，列，块对应的数字，遍历一次即可判断
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
    
        col_dict = {}
        block_dict = {}
        for i in xrange(len(board)):
            row_dict = [] # just a row
            if i/3 not in block_dict:
                block_dict[i/3] = {}
            for j in xrange(len(board[i])):
                if j not in col_dict:
                    col_dict[j] = []
                if j/3 not in block_dict[i/3]:
                    block_dict[i/3][j/3] = []
                    
                num = board[i][j]
                if num == '.':
                    continue
                
                # check row
                if num not in row_dict:
                    row_dict.append(num)
                else:
                    return False
                
                # check column
                if num not in col_dict[j]:
                    col_dict[j].append(num)
                else:
                    return False
                
                # check block
                if num not in block_dict[i/3][j/3]:
                    block_dict[i/3][j/3].append(num)
                else:
                    return False
            
        return True
                    
                
                
                
        