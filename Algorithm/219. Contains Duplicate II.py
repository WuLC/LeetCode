# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-11 13:13:12
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-11 13:13:21
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = {}
        for i in xrange(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = []
            count[nums[i]].append(i)
        
        for index in count.values():
            for j in xrange(1,len(index)):
                if index[j]-index[j-1] <= k:
                    return True
        return False