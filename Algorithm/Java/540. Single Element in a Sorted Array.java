/*
* @Author: WuLC
* @Date:   2017-08-09 14:34:53
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-09 14:35:13
* @Email: liangchaowu5@gmail.com
*/

// binary search
public class Solution
{
    public int singleNonDuplicate(int[] nums)
    {
        return helper(nums, 0, nums.length-1);
    }
    
    public int helper(int[] nums, int start, int end)
    {
        int mid = start + ((end - start) >> 1);
        if (mid - 1 >= start && nums[mid - 1] == nums[mid])
        {
            if ((mid - start - 1) % 2 != 0) return helper(nums, start, mid - 2);
            else return helper(nums, mid + 1, end);
        }
        else if(mid + 1 <= end && nums[mid + 1] == nums[mid])
        {
            if ((end - mid - 1) % 2 != 0) return helper(nums, mid + 2, end);
            else return helper(nums, start, mid - 1);
        }
        else return nums[mid];
    }
}