# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-09 15:38:15
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:27
# @Email: liangchaowu5@gmail.com


# 方案一,先排序再找，时间复杂度为O(n^3),超时
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # 先对list从小到大排序再遍历
        result = []

        if len(nums)<3:
            return result
            
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            else:
                for j in range(i+1,len(nums)-1):
                    if nums[i] + nums[j] >0:
                        break
                    else:
                        for k in range(j+1,len(nums)):
                            if nums[i] + nums[j] + nums[k] == 0:
                                tmp = [nums[i],nums[j],nums[k]]
                                if tmp not in result:
                                    result.append(tmp)
                            elif nums[i] + nums[j] + nums[k] >0:
                                break
        return result


# 方案二先排序再找，但是利用了双指针，时间复杂度为O(n^2)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        result = []
        nums.sort()
        while i<len(nums)-2:
            if nums[i]>0:
                break
            else:
                j = i+1
                k = len(nums)-1
                while j < k:
                    if nums[i]+nums[j]+nums[k]>0:
                        k-=1
                    elif nums[i]+nums[j]+nums[k]<0:
                        j+=1
                    else:
                        tmp = [nums[i],nums[j],nums[k]]
                        if tmp not in result:
                            result.append(tmp)
                        j+=1
                        k-=1
                i+=1
        return result





