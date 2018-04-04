/*
 * Created on Wed Apr 04 2018 19:44:51
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// record the max number and min number so far since number[i] may be negative
class Solution 
{
    public int maxProduct(int[] nums) 
    {
        int result = nums[0], currMax = nums[0], currMin = nums[0], tmpMax, tmpMin;
        for(int i=1; i<nums.length; i++)
        {
            tmpMax = Math.max(nums[i], Math.max(currMin*nums[i], currMax*nums[i]));
            tmpMin = Math.min(nums[i], Math.min(currMin*nums[i], currMax*nums[i]));
            result = Math.max(result, tmpMax);
            currMax = tmpMax;
            currMin = tmpMin;
        }
        return result;
    }
}