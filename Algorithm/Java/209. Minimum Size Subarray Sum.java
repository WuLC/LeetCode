/*
* @Author: WuLC
* @Date:   2017-08-03 22:43:16
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-03 22:43:32
* @Email: liangchaowu5@gmail.com
*/


// two pointers
public class Solution 
{
    public int minSubArrayLen(int s, int[] nums) 
    {
        int result = 0;
        int p1 = 0, p2 = 0;
        int sum = 0;
        while (p2 <= nums.length)
        {
            while(sum >= s)
            {
                if (result == 0) result = p2 - p1;
                else result = Math.min(p2 - p1, result);
                sum -= nums[p1];
                p1 += 1;
            }
            if (p2 == nums.length) break;
            sum += nums[p2];
            p2 += 1;
        }
        return result;
    }
}