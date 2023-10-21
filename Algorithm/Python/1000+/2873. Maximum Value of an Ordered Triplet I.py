class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        curr_max, max_diff = nums[0], [0]
        for i in range(1, len(nums)):
            curr_max = max(curr_max, nums[i])
            max_diff.append(curr_max - nums[i])
        
        curr_max, max_element = nums[-1], nums[:]
        for j in range(len(nums) - 1, -1, -1):
            curr_max = max(curr_max, nums[j])
            max_element[j] = curr_max
        
        return max(max_diff[i-1] * max_element[i] for i in range(1, len(nums)))
