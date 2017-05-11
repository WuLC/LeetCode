/**
* Author: WuLC
* Date:   2017-05-06 16:50:47
* Last modified by:   WuLC
* Last Modified time: 2017-05-06 16:52:24
* Email: liangchaowu5@gmail.com
*/

// count the number of 1 at each bit then mod 3 
// time O(n), more specific O(32n)
public class Solution 
{
    public int singleNumber(int[] nums) 
    {
        int result = 0, bit;
        for(int i = 0; i<32; i++)
        {
            bit = 0;
            for (int num:nums)
                if ((num & (1<<i)) != 0)
                    bit++;
            bit %= 3;
            result ^= (bit<<i);
        }
        return result;
    }
}