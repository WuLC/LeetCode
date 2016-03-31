class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        count = 0
        for i in range(1,len(nums)):
            if not nums[i] == nums[count]:
                count+=1
                nums[count]=nums[i]
        return count+1
        