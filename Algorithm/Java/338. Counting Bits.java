/*
* @Author: WuLC
* @Date:   2017-05-17 12:37:18
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-17 12:42:57
* @Email: liangchaowu5@gmail.com
*/

// bit manipulation and dp, time O(n)
// important rule: result[i] = result[i>>1] + (i&1);
public class Solution 
{
    public int[] countBits(int num) 
    {
        int[] result = new int[num+1];
        for(int i = 0; i <= num; i++)
            result[i] = result[i>>1] + (i&1);
        return result;
    }
}