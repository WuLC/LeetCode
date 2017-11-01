/*
 * Created on Wed Nov 01 2017 11:46:39
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp, dp[i][j] respresents the maximum length of repeated subarray of A[:i] and B[:j] that ends at A[i] and B[j]
// time complexity: O(mn), m is the length of 
class Solution 
{
    public int findLength(int[] A, int[] B) 
    {
        int m = A.length, n = B.length;
        int[][] dp = new int[m+1][n+1];
        int result = 0;
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                if (A[i] == B[j])
                    dp[i+1][j+1] = dp[i][j] + 1;
                result = Math.max(result, dp[i+1][j+1]);
            }
        }
        return result;
    }
}