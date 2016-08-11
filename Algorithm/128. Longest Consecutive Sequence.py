# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-11 14:52:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-11 15:09:04
# @Email: liangchaowu5@gmail.com

# method 1, use a set to store the number 
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, result = set(nums), 0
        for num in nums:
            ori, tmp = num, 0
            while num in s:
                tmp += 1
                s.remove(num)
                num += 1
            num = ori-1
            while num in s:
                tmp += 1
                s.remove(num)
                num -= 1
            result = max(result, tmp)
        return result

# method 2, hashtable, faster
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic, result = {}, 0
        for num in nums:
            if num not in dic:
                left = dic.get(num-1, 0)
                right = dic.get(num+1, 0)
                total = left + right + 1
                dic[num] = total
                result = max(result, dic[num])
                # update the left point and right point
                dic[num-left] = total
                dic[num+right] = total
        return result    