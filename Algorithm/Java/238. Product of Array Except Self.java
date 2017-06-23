/*
* @Author: WuLC
* @Date:   2017-06-23 09:36:40
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-23 09:42:41
* @Email: liangchaowu5@gmail.com
*/

// O(n) time, O(1)
// calculate left accumulated sum for each number firstly, then multiply by its right accumulated sum
public class Solution 
{
    public int[] productExceptSelf(int[] nums) 
    {
        int[] result = new int[nums.length];
        result[0] = 1;
        for(int i = 1; i < nums.length; i++)
            result[i] = result[i-1]*nums[i-1];
        int right = 1;
        for (int i = nums.length-1; i >= 0; i--)
        {
            result[i] *= right;
            right *= nums[i];
        }
        return result;
    }
}