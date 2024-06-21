# Solution 1, backtracking with dfs, TLE
class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0]
        def dfs(i, j, cnt, _sum):
            result[0] = max(cnt, result[0])
            if i >= j:
                return
            if nums[i]+nums[j] == _sum:
                dfs(i+1, j-1, cnt+1, _sum)
            if nums[i]+nums[i+1] == _sum:
                dfs(i+2, j, cnt+1, _sum)
            if nums[j]+nums[j-1] == _sum:
                dfs(i, j-2, cnt+1, _sum)
        
        n = len(nums)
        dfs(1, n-2, 1, nums[0]+nums[n-1])
        dfs(0, n-3, 1, nums[-2]+nums[-1])
        dfs(2, n-1, 1, nums[0]+nums[1])

        return result[0]

# Solution 2, dfs with cache
from collections import defaultdict

class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        memo = defaultdict(int)
        def dfs(i, j, _sum):
            if i >= j:
                return 0
            flag = (_sum, i, j)
            if flag in memo:
                return memo[flag]
            if nums[i]+nums[j] == _sum:
                memo[flag] = max(memo[flag], 1+dfs(i+1, j-1, _sum))
            if nums[i]+nums[i+1] == _sum:
                memo[flag] = max(memo[flag], 1+dfs(i+2, j, _sum))
            if nums[j]+nums[j-1] == _sum:
                memo[flag] = max(memo[flag], 1+dfs(i, j-2, _sum))
            return memo[flag]
        
        return 1+max(dfs(1, n-2, nums[0]+nums[n-1]),
                max(dfs(0, n-3, nums[-2]+nums[-1]),
                    dfs(2, n-1, nums[0]+nums[1]))
        )


