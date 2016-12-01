/**
* Author: LC
* Date:   2016-12-01 20:40:22
* Last modified by:   WuLC
* Last Modified time: 2016-12-01 20:44:11
* Email: liangchaowu5@gmail.com
*/

// recursive binary search 
// O(n) time for worse case when  there are duplicate characters in the string
// search in just one part when assure that the target is in that part, else search in both parts
public class Solution 
{
    public boolean search(int[] nums, int target) 
    {
        return helper(nums, target, 0, nums.length-1);
    }
    
    public boolean helper(int[] nums, int target, int left, int right)
    {
        if (left > right) return false;
        else if(left == right)
        {
            if (nums[left] == target) return true;
            else return false;
        }
        else
        {
            int mid = left + ((right-left)>>1);
            if (nums[mid] == target) return true;
            else if(nums[mid] > nums[left] && nums[mid] > target && target >= nums[left]) return helper(nums, target, left, mid-1);
            else if(nums[mid] < nums[right] && nums[mid] < target && target <= nums[right]) return helper(nums, target, mid+1, right);
            else return helper(nums, target, left, mid-1) || helper(nums, target, mid+1, right);
        }
    }
}