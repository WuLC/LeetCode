# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-01 10:37:02
# @Last Modified by:   WuLC
# @Last Modified time: 2017-05-01 10:44:18


# simple code,but cost more memory
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums)*len(nums[0]) != r*c:
            return nums
        arrs = []
        for arr in nums:
            arrs += arr
        result = []
        for i in xrange(r):
            result.append(arrs[i*c: (i+1)*c])
        return result
            
            
            
# little complex code, but cost fewer memory
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums)*len(nums[0]) != r*c:
            return nums
        rows, cols = len(nums), len(nums[0]) 
        result = []
        curr_r, curr_c = 0, 0 
        for i in xrange(r):
            tmp = []
            for j in xrange(c):
                if curr_c == cols:
                    curr_r += 1
                    curr_c = 0
                if curr_r == rows:
                    break
                tmp.append(nums[curr_r][curr_c])
                curr_c += 1
            result.append(tmp[:])
        return result