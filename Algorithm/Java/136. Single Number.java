/**
* Author: WuLC
* Date:   2017-05-06 16:07:59
* Last modified by:   WuLC
* Last Modified time: 2017-05-06 16:08:27
* Email: liangchaowu5@gmail.com
*/


// bit manipulation

public class Solution 
{
    public int singleNumber(int[] nums) 
    {
        int result = 0;
        for(int num : nums)
            result ^= num;
        return result;
    }
}