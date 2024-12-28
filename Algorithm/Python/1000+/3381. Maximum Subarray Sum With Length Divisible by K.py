# naive solution, O(n^2) time complexity, TLE
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n, pre_sum = len(nums), [0]
        for i in range(n):
            pre_sum.append(pre_sum[-1] + nums[i])
        
        result = -1* n * (10**9)
        for i in range(n):
            for j in range(1, int(i/k)+2):
                if i - j*k + 1 >= 0:
                    result = max(result, pre_sum[i+1] - pre_sum[i - j*k + 1])
        return result

# optimized solution, time complexity O(n)
# store min(pre_sum[i], pre_sum[i-k], pre_sum[i-2*k]....pre_sum[i-n*k]) in the first element pre_sum[i%k]
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n, pre_sum = len(nums), [0]
        for i in range(n):
            pre_sum.append(pre_sum[-1] + nums[i])
        
        result = -1 * n * (10**9)
        for i in range(k-1, n): # need to start from k-1
            result = max(result, pre_sum[i+1] - pre_sum[(i+1)%k])
            pre_sum[(i+1)%k] = min(pre_sum[(i+1)%k], pre_sum[i+1])
        return result
        

