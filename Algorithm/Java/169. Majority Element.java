/*
* @Author: WuLC
* @Date:   2017-05-26 14:55:00
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-26 14:55:57
* @Email: liangchaowu5@gmail.com
*/

// Boyer–Moore majority vote algorithm
// O(n) time, O(1) space
public class Solution 
{
    public int majorityElement(int[] nums) 
    {
        int num = 0, count = 0;
        for (int n : nums)
        {
            if (count == 0) 
            {
                num = n;
                count++;
            }
            else if(num != n) count--;
            else count++;
        }
        return num;
    }
}