# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-01 20:37:36
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-01 20:41:36
# @Email: liangchaowu5@gmail.com

# referer: https://www.hrwhisper.me/leetcode-increasing-triplet-subsequence/
# n1 is the smallest element so far
# n2 is the smallest element that has at least a smaller element so far
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n1, n2 = None, None
        for num in nums:
            if n1 == None or num<n1:
                n1 = num
            elif num>n1 and (n2== None or n2>num):
                n2 = num
            elif n2!= None and num > n2:
                return True
        return False
                
                