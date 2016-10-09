# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-24 20:40:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-24 20:40:52
# @Email: liangchaowu5@gmail.com

# two pointers, O(n) time complexity
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, count, n = 0, 0, 0, len(nums)
        length = n+1
        while right < n:
            while count < s and right < n:
                count += nums[right]
                right += 1
            if right > n:
                break
            while left<right and count >= s:
                length = min(length, right - left)
                count -= nums[left]
                left += 1
        return length if length!=n+1 else 0
        