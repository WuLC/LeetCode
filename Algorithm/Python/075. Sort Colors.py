# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-14 16:34:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-14 19:46:14
# @Email: liangchaowu5@gmail.com

# method1 ,count the number of 0,1,2 in the list
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = {0:0,1:0,2:0}
        for i in xrange(n):
            tmp[nums[i]] += 1
        cur = 0
        for j in xrange(3):
            for k in xrange(tmp[j]):
                nums[cur] = j
                cur += 1
            
        
# method2, three pointers
# referer: https://en.wikipedia.org/wiki/Dutch_national_flag_problem      
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, n = 0, 0, len(nums)-1
        while j <= n:
            if nums[j] > 1:
                nums[n], nums[j] = nums[j], nums[n]
                n -= 1
            elif nums[j] == 1:
                j+=1
            elif nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        
