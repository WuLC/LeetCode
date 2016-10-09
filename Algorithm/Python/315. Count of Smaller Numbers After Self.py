# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-10 14:18:41
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-10 14:19:24
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0 for i in xrange(len(nums))]
        enum = list(enumerate(nums))
        self.merge_sort(enum, count)
        return count
        
    def merge_sort(self, enum, count):
        mid = len(enum)/2
        if mid > 0:
            left, right = self.merge_sort(enum[:mid], count), self.merge_sort(enum[mid:], count)
            i, j, m, n =0, 0, len(left), len(right)
            while i<m or j<n:
                if j==n or i<m and left[i][1] <= right[j][1]:
                    enum[i+j] = left[i]
                    count[left[i][0]] += j
                    i += 1
                else:
                    enum[i+j] = right[j]
                    j += 1
        return enum