/**
* Author: WuLC
* Date:   2017-02-06 16:55:17
* Last modified by:   WuLC
* Last Modified time: 2017-02-06 16:57:00
* Email: liangchaowu5@gmail.com
*/

// bit manipulation
public class Solution 
{
    public int findComplement(int num) 
    {
        int tmp = num, bitCount = 0;
        while (tmp!=0)
        {
            tmp >>= 1;
            bitCount++;
        }
        return (~num)& ((1<<bitCount)-1);
    }
}