/*
* @Author: WuLC
* @Date:   2017-01-18 00:01:41
* @Last Modified by:   WuLC
* @Last Modified time: 2017-01-18 00:03:26
* @Email: liangchaowu5@gmail.com
*/

// xor the two numbers and count the number of 1 in the number
public class Solution 
{
    public int hammingDistance(int x, int y) 
    {
        int result = x^y;
        int count = 0;
        while (result!=0)
        {
            if ((result&1)!=0) count++;
            result >>= 1;
        }
        return count;
    }
}