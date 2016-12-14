/**
* Author: WuLC
* Date:   2016-12-14 22:27:26
* Last modified by:   WuLC
* Last Modified time: 2016-12-14 22:28:44
* Email: liangchaowu5@gmail.com
*/


// greedy, similar to problem 55. Jump Games
public class Solution 
{
    public int jump(int[] nums) 
    {
        if (nums.length <= 1) return 0;
        int currMax = nums[0], nextMax = 0, count = 1;
        for(int i = 1; i < nums.length; i++)
        {
            if (currMax >= nums.length-1) break;
            nextMax = Math.max(nextMax, i+nums[i]);
            if(i==currMax)
            {
                count += 1;
                currMax = nextMax;
            }
        }
        return count;
    }
}