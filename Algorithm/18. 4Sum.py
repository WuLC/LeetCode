#encoding:utf-8
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result =[]
        if len(nums) == 0:
            return result
        
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                m = j +1
                n = len(nums)-1
                while m < n:
                    sum = nums[i] + nums[j] + nums[m] + nums[n]
                    if  sum>target:
                        n-=1
                    elif sum<target:
                        m+=1
                    else:
                        tmp = [nums[i],nums[j],nums[m],nums[n]]
                        if tmp not in result:
                            result.append(tmp)
                        m+=1
                        n-=1
        return result
        