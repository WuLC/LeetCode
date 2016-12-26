/**
* Author: LC
* Date:   2016-12-26 22:06:04
* Last modified by:   WuLC
* Last Modified time: 2016-12-26 22:06:16
* Email: liangchaowu5@gmail.com
*/


// dp
public class Solution 
{
    public int maxSubArray(int[] nums) 
    {
        if (nums.length == 0) return 0;
        int result = nums[0], previousMax = nums[0], currMax;
        for(int i = 1;i < nums.length; i++)
        {
            currMax = Math.max(nums[i], nums[i]+previousMax);
            result = Math.max(currMax, result);
            previousMax = currMax;
        }
        return result;
    }
}