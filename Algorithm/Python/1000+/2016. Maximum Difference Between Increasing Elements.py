class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prefix_min, curr_min = [nums[0]], nums[0]
        for i in range(1, len(nums)):
            curr_min = min(curr_min, nums[i])
            prefix_min.append(curr_min)
        
        result,curr_max = -1, nums[-1]
        for i in range(len(nums)-1, 0, -1):
            curr_max = max(curr_max, nums[i])
            if curr_max - prefix_min[i-1] > 0:
                result = max(result, curr_max - prefix_min[i-1])
        return result
