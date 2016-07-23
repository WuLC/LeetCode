# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-23 14:37:57
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-23 21:42:58
# @Email: liangchaowu5@gmail.com

# method 1
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.count = [0 for i in xrange(len(nums))]
        for i in xrange(len(nums)):
            if i == 0:
                self.count[0] = nums[0]
            else:
                for j in xrange(i-self.lowest_bit(i)+1, i+1):
                    self.count[i] += nums[j]
       
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if i==0:
            self.nums[0] = val
            self.count[0] = val
        else:
            diff = self.nums[i] - val
            self.nums[i] = val
            while i < len(self.nums):
                self.count[i] -= diff
                i += self.lowest_bit(i)
            

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==j:
            return self.nums[i]
        else:
            idx, i_sum, j_sum =i, 0, 0
            while i > 0:
                i_sum += self.count[i]
                i -= self.lowest_bit(i)
            while j>0:
                j_sum += self.count[j]
                j -= self.lowest_bit(j)
            if idx == 0:
                return j_sum+self.count[0]
            else:
                return j_sum - i_sum + self.nums[idx]
        
    def lowest_bit(self, num):
        return num&(-num)
        

# method 2,make the above code more concise
# the above code take 0 as an exception, the following generalize it by adding one more element to count
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.count = [0 for i in xrange(len(nums)+1)]
        for i in xrange(len(nums)):
            self.initialize(i, nums[i])
    
    def initialize(self, i, val):
        i += 1
        while i < len(self.nums)+1:
            self.count[i] += val
            i += (i & -i)
        
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.initialize(i, diff)
    
    def left_sum(self, i):
        i += 1
        total = 0
        while i>0:
            total += self.count[i]
            i -= (i & -i)
        return total

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.left_sum(j) - self.left_sum(i-1)