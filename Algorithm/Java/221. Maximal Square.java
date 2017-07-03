/*
* @Author: WuLC
* @Date:   2017-07-03 19:25:27
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-03 19:28:43
* @Email: liangchaowu5@gmail.com
*/


// dp
// dp[i][j] represents the edge length of the square whose bottom right point is (i, j)
public class Solution 
{
    public int maximalSquare(char[][] matrix) 
    {
        if (matrix.length == 0) return 0;
        int m = matrix.length, n = matrix[0].length;
        int[][] dp = new int[m+1][n+1];
        int len = 0;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(matrix[i][j] == '1')
                {
                    dp[i+1][j+1] = Math.min(Math.min(dp[i][j], dp[i][j+1]), dp[i+1][j]) + 1;
                    len = Math.max(len, dp[i+1][j+1]);
                }
            }
        }
        return len*len;
    }
}