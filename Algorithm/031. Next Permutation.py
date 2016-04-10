# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-04 11:13:21
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:22:46
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sortList = sorted(nums)
        if nums == sortList[::-1]:
            nums.sort()
            return
        
        i = len(nums)-1
        flag = 0
        while i > 0:
            if nums[i] > nums[i-1]:
                # 从后往前找大于nums[i-1]且小于nums[i]的数与nums[i-1]交换
                if not i==len(nums)-1:
                    j = i+1
                    while j<len(nums):
                        if nums[i-1]<nums[j]<nums[i]:
                            nums[j],nums[i-1] = nums[i-1],nums[j]
                            flag = 1
                            break
                        j+=1
                        
                # 找不到这样的数
                if flag == 0:
                    nums[i],nums[i-1] = nums[i-1],nums[i]
                
                # 交换后对i后面的元素从小到大进行排序
                nums[i:] = sorted(nums[i:])
                return                 
            else:
                i-=1