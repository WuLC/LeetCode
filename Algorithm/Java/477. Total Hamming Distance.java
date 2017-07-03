/*
* @Author: WuLC
* @Date:   2017-07-03 12:53:22
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-03 12:54:56
* @Email: liangchaowu5@gmail.com
*/

// deal with one bit for all numbers
public class Solution 
{
    public int totalHammingDistance(int[] nums) 
    {
        int count = 0;
        for (int i = 0; i < 32; i++)
        {
            int zero = 0, one = 0;
            for (int num : nums)
            {
                if((num & (1 << i)) == 0) zero++;
                else one++;
            }
            count += one*zero;
        }
        return count;
    }
}