/**
* Author: LC
* Date:   2016-12-14 21:13:34
* Last modified by:   WuLC
* Last Modified time: 2016-12-14 21:17:56
* Email: liangchaowu5@gmail.com
*/


// greedy, find the longest distance that we can reach so far 
public class Solution 
{
    public boolean canJump(int[] nums) 
    {
        if (nums.length <= 1) return true;
        int currMax = nums[0], idx = 1;
        while(idx <= currMax)
        {
            if (currMax >= nums.length - 1) return true;
            currMax = Math.max(currMax, nums[idx] + idx );
            idx += 1;
        }
        return false;
    }
}