/**
* Author: WuLC
* Date:   2016-12-02 11:16:25
* Last modified by:   WuLC
* Last Modified time: 2016-12-02 11:17:20
* Email: liangchaowu5@gmail.com
*/


// binary search
public class Solution 
{
    public int searchInsert(int[] nums, int target) 
    {
        if (nums.length == 0) return 0;
        int left = 0, right = nums.length-1, mid;
        while (left < right)
        {
            mid = left + ((right-left)>>1);
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) left = mid + 1;
            else right = mid -1;
        }
        if (nums[left] >= target) return left;
        else return left+1;
    }
}