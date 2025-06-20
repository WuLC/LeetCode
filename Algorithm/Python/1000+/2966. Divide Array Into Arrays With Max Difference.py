class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        idx, n = 0, len(nums)
        while idx < n:
            if nums[idx+2] - nums[idx] > k:
                return []
            idx += 3
        return [nums[i:i+3] for i in range(0, n-2, 3)]