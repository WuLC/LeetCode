/**
* Author: WuLC
* Date:   2017-04-29 11:10:15
* Last modified by:   WuLC
* Last Modified time: 2017-04-29 11:53:15
* Email: liangchaowu5@gmail.com
*/


// dp, dp[i] represents the length of longest subsequence that ends with nums[i]
// O(n^2) time, O(n) space
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

// dp, dp[i] represents the smallest number among those numbers 
// that act as the last number of the increasing subsequence of length i+1
// O(nlogn) time, O(n) space
public class Solution 
{
    public int lengthOfLIS(int[] nums) 
    {
        int currLen = -1;
        int[] dp = new int[nums.length];
        for(int i=0; i<nums.length; i++)
        {
            if (currLen == -1 || nums[i] > dp[currLen])
            {
                currLen++;
                dp[currLen] = nums[i];
            }
            else
            {   // binary search
                int left = 0, right = currLen, mid = 0;
                while (left < right)
                {
                    mid = left + ((right-left)>>1);
                    if (nums[i] == dp[mid]) break;
                    else if(nums[i] > dp[mid]) left = mid+1;
                    else right = mid;
                }
                dp[left] = Math.min(dp[left], nums[i]);
            }
        }
        return currLen+1;
    }
}