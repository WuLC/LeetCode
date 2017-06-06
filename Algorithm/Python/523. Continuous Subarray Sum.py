# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-05 23:06:01
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-07 00:02:49
# @Email: liangchaowu5@gmail.com


# naive dp, O(n^2), almost TLE
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dp = [set() for _ in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            dp[i-1].add(nums[i-1])
            for num in dp[i-1]:
                curr_sum = nums[i] + num
                if curr_sum == k or (k!= 0 and curr_sum % k == 0):
                    return True
                dp[i].add(curr_sum)
        return False
                
            

# presum + hashtable, O(n)
# referer: https://discuss.leetcode.com/topic/80793/java-o-n-time-o-k-space
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """ 
        mapping = {0:-1} # deal with the case which there is only two elements
        count = 0
        for i in xrange(len(nums)):
            count += nums[i]
            if k != 0: count %= k
            if count in mapping:
                if i - mapping[count] > 1:
                    return True
            else:
                mapping[count] = i
        return False

         
