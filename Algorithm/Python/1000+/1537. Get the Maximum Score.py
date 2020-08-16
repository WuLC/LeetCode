
# dp, time O(mn), TLE
class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        # construct dp matrix
        dp1, dp2 = [[0]*(n+1) for _ in range(m+1)], [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            dp1[i+1][0] = dp1[i][0] + nums1[i]
        for j in range(n):
            dp2[0][j+1] = dp2[0][j] + nums2[j]
                
        index1, index2 = {}, {}
        for i in range(m):
            val1 = nums1[i]
            index1[val1] = i
            for j in range(n):
                val2 = nums2[j]
                index2[val2] = j
                dp1[i+1][j+1] = max(dp1[i+1][j+1], dp1[i][j+1] + val1)
                dp2[i+1][j+1] = max(dp2[i+1][j+1], dp2[i+1][j] + val2) 
                # update dp1
                if val1 in index2:
                    dp1[i+1][j+1] = max(dp1[i+1][j+1], dp2[i][index2[val1]+1]) 
                # update dp2
                if val2 in index1:
                    dp2[i+1][j+1] =  max(dp2[i+1][j+1], dp1[index1[val2]+1][j])   
                dp1[i+1][j+1] %= 1000000007
                dp2[i+1][j+1] %= 1000000007
        return max(dp1[m][n], dp2[m][n])


# two pointers
class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        curr_sum1, curr_sum2 = 0, 0
        while idx1 < m or idx2 < n:
            if idx1 < m  and (idx2 == n or nums1[idx1] < nums2[idx2]):
                curr_sum1 += nums1[idx1]
                idx1 += 1
            elif idx2 < n and (idx1 == m or nums1[idx1] > nums2[idx2]):
                curr_sum2 += nums2[idx2]
                idx2 += 1
            else:
                curr_sum1 = curr_sum2 = max(curr_sum1, curr_sum2) + nums1[idx1]
                idx1 += 1
                idx2 += 1
        return max(curr_sum1, curr_sum2) % 1000000007
            
