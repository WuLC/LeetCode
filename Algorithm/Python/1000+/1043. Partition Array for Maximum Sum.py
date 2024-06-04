class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0] * (n+1)
        for i in range(n):
            max_num, cnt = arr[i], 0
            while cnt < k and i-cnt >= 0:
                max_num = max(max_num, arr[i-cnt])
                dp[i+1] = max(dp[i-cnt] + max_num*(cnt+1), dp[i+1])
                cnt += 1
        return dp[-1]