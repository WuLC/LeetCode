/**
* Author: WuLC
* Date:   2017-04-29 11:10:15
* Last modified by:   WuLC
* Last Modified time: 2017-04-29 11:10:44
* Email: liangchaowu5@gmail.com
*/


// dp, O(n^2) time, O(n) space
public class Solution 
{
    public int lengthOfLIS(int[] nums) 
    {
        int result = 0;
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        for(int i=0; i<nums.length; i++)
        {
            for(int j=0; j<i; j++)
                if (nums[i] > nums[j]) 
                    dp[i] = Math.max(dp[i], dp[j]+1);
            result = Math.max(result, dp[i]);
        }
        return result;
    }
}