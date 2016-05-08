# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-08 09:31:46
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-08 15:23:48
# @Email: liangchaowu5@gmail.com


# 利用nextPermutation，TLE >_<
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in xrange(1,n+1)]
        for i in xrange(k-1):
            self.nextPermutation(nums)
        return reduce(lambda x,y:str(x)+str(y),nums)

    def nextPermutation(self, nums):
        sortList = sorted(nums)
        if nums == sortList[::-1]:
            nums.sort()
            return
        
        i = len(nums)-1
        flag = 0
        while i > 0:
            if nums[i] > nums[i-1]:
                # 往后找大于nums[i-1]且小于nums[i]的数与nums[i-1]交换
                j = len(nums)-1
                while j>i:
                    if nums[i-1]<nums[j]<nums[i]:
                        nums[j],nums[i-1] = nums[i-1],nums[j]
                        flag = 1
                        break
                    j-=1
                # 找不到这样的数
                if flag == 0:
                    nums[i],nums[i-1] = nums[i-1],nums[i]
                # 交换后对i后面的元素进行排序
                nums[i:] = sorted(nums[i:])
                return                 
            else:
                i-=1


# 参考https://leetcode.com/discuss/47086/share-my-python-solution-with-detailed-explanation，AC 
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1,n+1)
        k -= 1  # 不减1会导致k为最后一个数时越界
        res = ''
        while n > 0:
            n -= 1
            index, k = divmod(k,math.factorial(n)) # 0! = 1，0%n = 0
            res += str(nums.pop(index))
        return res
        