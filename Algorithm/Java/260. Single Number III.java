/**
* Author: LC
* Date:   2017-05-14 23:37:07
* Last modified by:   WuLC
* Last Modified time: 2017-05-14 23:40:22
* Email: liangchaowu5@gmail.com
*/


// xor all the numbers to get mix
// the lowest bit of mix represents the lowest different bit between the two numbers
// split all the numbers into two parts in terms of this bit, each part must contains one of the numbers

public class Solution 
{
    public int[] singleNumber(int[] nums) 
    {
        int mix = 0;
        for(int num:nums) mix ^= num;
        int lowBit = mix & (-mix);
        int num1 = 0, num2 = 0;
        for(int num:nums)
        {
            if ((num & lowBit) != 0) num1 ^= num;
            else num2 ^= num;
        }
        return new int[]{num1, num2};
    }
}