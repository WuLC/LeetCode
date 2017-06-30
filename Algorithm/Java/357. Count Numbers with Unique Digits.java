/*
* @Author: WuLC
* @Date:   2017-06-30 15:31:36
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-30 15:47:22
* @Email: liangchaowu5@gmail.com
*/

// dp
// dp[i] represents the result of number within(<=) i bits
public class Solution 
{
    public int countNumbersWithUniqueDigits(int n) 
    {
        int[] dp = new int[n+1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++)
        {
            int bits = i;
            int count = 1;
            int choices = 9;
            while (bits > 0)
            {
                count *= choices;
                if(bits != i) choices--; // 0 is not allowed to be the left most bit but is allowed on other bits
                bits--;
            }
            dp[i] = dp[i-1] + count;
        }
        return dp[n];
    }
}


// remove the dp array above 
// calculate the result of number that has 2,3...n bits and add them up
public class Solution 
{
    public int countNumbersWithUniqueDigits(int n) 
    {
        int curNum = 9;
        int sumNum = 10;
        int availableNum = 9;
        if(n == 0) return 1;

        // calculate the result of number that has 2,3...n bits and add them up
        while(curNum >= 1 && n > 1) 
        {
            curNum = curNum * availableNum;
            sumNum += curNum;
            availableNum--;
            n--;
        }
        return sumNum;
    }
}