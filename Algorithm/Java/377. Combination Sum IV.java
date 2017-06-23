/*
* @Author: WuLC
* @Date:   2017-06-23 18:55:53
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-23 19:00:30
* @Email: liangchaowu5@gmail.com
*/


// dynamic programming
// dp[i] represents the number of combination sum for number i
public class Solution 
{
    public int combinationSum4(int[] nums, int target) 
    {
        int[] dp = new int[target+1];
        dp[0] = 1;
        Arrays.sort(nums);
        int count;
        for (int i = 1; i <= target; i++)
        {
            count = 0;
            for (int j = 0; j < nums.length; j++)
            {
                if (nums[j] > i) break;
                count += dp[i - nums[j]];
            }
            dp[i] = count;
        }
        return dp[target];
    }
}