/**
* Author: LC
* Date:   2017-05-26 14:14:58
* Last modified by:   WuLC
* Last Modified time: 2017-05-26 14:34:35
* Email: liangchaowu5@gmail.com
*/

// dp
// dp[i] represents the max money that can robbed from with the first i houses
// dp[i] = max(dp[i-1], dp[i-2] + nums[i])
// compress it to O(1) space by representing dp[i-1] = curr and dp[i-1] = pre
public class Solution 
{
    public int rob(int[] nums) 
    {
        int curr = 0, pre = 0, tmp;
        for (int i = 0; i < nums.length; i++) 
        {
            tmp = curr;
            curr =Math.max(pre + nums[i], curr);
            pre = tmp;
        }
        return Math.max(curr, pre);
    }
}


// dp
// dp[i] represents the max money that can robbed from with the first i houses, and the i-th  house must be robbed
// dp[i] = max(dp[i-3], dp[i-2])+nums[i]
// O(n) space
public class Solution 
{
    public int rob(int[] nums) 
    {
        if (nums.length == 0) return 0;
        int n = nums.length;
        int[] dp = new int[n+1];
        for (int i = 0; i < n; i++) 
        {
            if (i < 2) dp[i+1] = nums[i];
            else dp[i+1] = Math.max(dp[i-1], dp[i-2]) + nums[i];
        }
        return Math.max(dp[n], dp[n-1]);
    }
}