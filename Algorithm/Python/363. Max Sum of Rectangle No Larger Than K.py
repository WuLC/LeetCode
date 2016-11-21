# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-21 14:55:26
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-21 16:18:29
# @Email: liangchaowu5@gmail.com

# base on max subarray no larger than k in 1-D array and max sum of rectangle in an 2-D matrix
# referer:
# https://discuss.leetcode.com/topic/48875/accepted-c-codes-with-explanation-and-references
# https://www.youtube.com/watch?v=yCQN096CwWM
# https://www.quora.com/Given-an-array-of-integers-A-and-an-integer-k-find-a-subarray-that-contains-the-largest-sum-subject-to-a-constraint-that-the-sum-is-less-than-k


# brute force, TLE
# time complexity O((row*col)^2)
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        result = None
        for left in xrange(n):
            sums = [0 for i in xrange(m)]
            for right in xrange(left, n):
                for i in xrange(m):
                    sums[i] += matrix[i][right]
                cumulative_sum, curr_sum = [0], 0
                for i in xrange(m):
                    curr_sum += sums[i]
                    for cs in cumulative_sum:
                        if curr_sum-cs <= k  and (result == None or result < curr_sum-cs):
                            result = curr_sum - cs
                    cumulative_sum.append(curr_sum)
        return result
                        
                
# same idea as above, but with module bisect makes it faster
# AC(1276ms), time complexity O(col^2*row*log(row))
import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        result = -pow(2,31)
        for left in xrange(n):
            sums = [0 for i in xrange(m)]
            for right in xrange(left, n):
                for i in xrange(m):
                    sums[i] += matrix[i][right]
                cumulative_sum, curr_sum = [0], 0
                for i in xrange(m):
                    curr_sum += sums[i]
                    index = bisect.bisect_left(cumulative_sum, curr_sum - k) # binary search
                    if index != len(cumulative_sum):
                        result = max(result, curr_sum - cumulative_sum[index])
                    bisect.insort(cumulative_sum, curr_sum)                 # binary search
        return result