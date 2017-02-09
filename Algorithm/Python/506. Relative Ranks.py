# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-09 20:56:51
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-09 20:57:47
# @Email: liangchaowu5@gmail.com


# sort and store the sorted list in hashmap, O(nlogn) time, O(n) space
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortedNums = sorted(nums, reverse=True)
        numsMap = {}
        for i in xrange(len(sortedNums)):
            if i == 0:
                numsMap[sortedNums[i]] = 'Gold Medal'
            elif i == 1:
                numsMap[sortedNums[i]] = 'Silver Medal'
            elif i == 2:
                numsMap[sortedNums[i]] = 'Bronze Medal'
            else:
                numsMap[sortedNums[i]] = str(i+1)
        result = []
        for num in nums:
            result.append(numsMap[num])
        return result
                
                
            