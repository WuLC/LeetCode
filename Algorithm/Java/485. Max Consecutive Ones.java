/**
* Author: WuLC
* Date:   2017-02-03 22:25:27
* Last modified by:   WuLC
* Last Modified time: 2017-02-03 22:25:41
* Email: liangchaowu5@gmail.com
*/

// O(1) dp
public class Solution 
{
    public int findMaxConsecutiveOnes(int[] nums) 
    {
       int result = 0, currMax = 0;
       for(int i=0; i<nums.length; i++)
       {
           if (nums[i] == 0) currMax = 0;
           else currMax++;
           result = Math.max(result, currMax);
       }
       return result;
    }
}