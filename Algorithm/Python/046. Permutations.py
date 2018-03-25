# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-04 14:48:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-06 15:36:30
# @Email: liangchaowu5@gmail.com

# 方法一:backtracking
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums,0,result)
        return result
        
    def helper(self, nums, begin, result):
        n = len(nums)
        if begin == n:
            tmp = nums[:]
            result.append(tmp)
            return
        
        for i in xrange(begin,n):
            nums[begin],nums[i] = nums[i], nums[begin]
            self.helper(nums,begin+1,result)
            nums[begin],nums[i] = nums[i], nums[begin]

# 方法二:直接进行排列,每次插入一个新的数字
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            new_result = []
            for seq in result:
                for i in xrange(len(seq)+1):
                    new_result.append(seq[:i]+[num]+seq[i:])
            result = new_result
        return result
                    
# divide and conquer
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 1:
            result.append(nums)
        else:
            for i in xrange(len(nums)):
                for left in self.permute(nums[:i]+nums[i+1:]):
                    result.append([nums[i]]+left)
        return result

if __name__ == '__main__':
    test = [1,2,3,4]
    s = Solution()
    res = s.permute(test)
    for i in res:
        print i