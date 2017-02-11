# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-11 16:11:18
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-11 16:14:19
# @Email: liangchaowu5@gmail.com


# stack and hashmap
# store the greater numbers in the list as the values of hashmap
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        numsMap = collections.defaultdict(list)
        for num in nums:
            while stack and stack[-1] < num:
                numsMap[stack.pop()].append(num)
            stack.append(num)
        for num in nums:
            while len(stack) > 1 and stack[-1] < num:
                numsMap[stack.pop()].append(num)
        result = [0 for i in xrange(len(nums))]
        for i in reversed(xrange(len(nums))):
            result[i] = numsMap[nums[i]].pop() if nums[i] in numsMap else -1
        return result