# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-04-20 09:21:22
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-22 10:17:45
# @Email: liangchaowu5@gmail.com


# DP,超时
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp=[]
        dp.append(0)
        for i in xrange(1,n):
            min = None
            for j in range(i):
                if j+nums[j]==i:
                    tmp = dp[j]+1
                else:
                    tmp = dp[j]+i-j
                if min==None or min>tmp:
                    min = tmp
            dp.append(min)
        return dp[n-1]

#greedy,AC
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        n = len(nums)
        current_reach_max = nums[0]
        max_reach = nums[0]
        steps = 1
        i=0
        while i<=min(n,max_reach):
            current_reach_max = max(current_reach_max,i+nums[i])
            if i==n-1:
                return steps
            if i==max_reach:
                max_reach = current_reach_max
                steps+=1
            i+=1
                