# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-08 20:27:23
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-08 20:50:59
# @Email: liangchaowu5@gmail.com

# naive solution, O(mn) time, O(1) space, AC
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for findNum in findNums:
            tmp = -1
            find = False
            for i in xrange(len(nums)):
                if findNum == nums[i]:
                    find = True
                if find and nums[i] > findNum:
                    tmp = nums[i]
                    break
            result.append(tmp)
        return result


# stack and hashmap, O(n) time, O(n) space
# traverse from left to right
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        stack = []
        numsMap = {}
        for num in nums:
            while stack and stack[-1] < num:
                numsMap[stack.pop()] = num
            stack.append(num)
        for num in findNums:
            if num in numsMap:
                result.append(numsMap[num])
            else:
                result.append(-1)
        return result


# stack and hashmap, O(n) time, O(n) space
# traverse from right to left
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        record, stack =  {}, []
        for i in xrange(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack:
                record[nums2[i]] = stack[-1]
            else:
                record[nums2[i]] = -1
            stack.append(nums2[i])
        return [record[num] for num in nums1]