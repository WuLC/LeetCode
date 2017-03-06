# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-06 14:59:16
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-06 14:59:55
# @Email: liangchaowu5@gmail.com


# pay attention that k is just an integer, it can be 0 or negative number
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        if k < 0: 
            return 0
        elif k==0:
            mapping = collections.defaultdict(int)
            for num in nums:
                mapping[num] += 1
            for k,v in mapping.items():
                if v >= 2:
                    count +=1
        else:
            nums = set(nums)
            for num in nums:
                if num+k in nums:
                    count += 1
        return count