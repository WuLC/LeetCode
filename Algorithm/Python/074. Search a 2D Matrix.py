# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-14 14:38:29
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-14 14:38:37
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m>0:
            n = len(matrix[0])
            if n == 0:
                return False
        else:
            return False
        
        left, right = 0, m-1
        while left < right:
            mid = (left + right) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target <= matrix[mid][n-1]:
                left = mid
                break
            else:
                left = mid+1
        r = left 
        left, right = 0, n-1
        while left < right:
            mid = (left+right)/2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] > target:
                right = mid - 1
            elif matrix[r][mid] < target:
                left = mid + 1
        if matrix[r][left] == target:
            return True
        else:
            return False