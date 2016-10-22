/**
* Author: WuLC
* Date:   2016-10-22 19:37:36
* Last modified by:   WuLC
* Last Modified time: 2016-10-22 19:38:13
* Email: liangchaowu5@gmail.com
*/


// two pointers, always keep the higher edge
public class Solution 
{
    public int maxArea(int[] height) 
    {
        int left = 0, right = height.length - 1;
        int result = 0;
        while (left < right)
        {
            result = Math.max(result, Math.min(height[left], height[right])*(right-left));
            if (height[left] > height[right]) right--;
            else left++;
        }
        return result;
    }
}