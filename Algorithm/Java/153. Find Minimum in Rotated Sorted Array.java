/*
* @Author: WuLC
* @Date:   2017-05-27 11:56:13
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-27 11:56:44
* @Email: liangchaowu5@gmail.com
*/


// binary search, pay attention that one half must be in order
public class Solution 
{
    public int findMin(int[] nums) 
    {
        int left = 0 , right = nums.length - 1, mid;
        while (left < right)
        {
            mid = left + ((right - left) >> 1);
            if (nums[right] > nums[mid]) right = mid;
            else left = mid + 1;
        }
        return nums[left];
    }
}