/*
* @Author: WuLC
* @Date:   2017-07-14 08:54:58
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-14 21:42:03
* @Email: liangchaowu5@gmail.com
*/


// referer: https://discuss.leetcode.com/topic/12133/bit-operation-solution-java
// if m != n, the rightmost bit must be 0
public class Solution 
{
    public int rangeBitwiseAnd(int m, int n) 
    {
        int  count = 1;
        while(m != n)
        {
            m >>= 1;
            n >>= 1;
            count <<= 1;
        }
        return m * count;
    }
}