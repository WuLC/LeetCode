/**
* Author: LC
* Date:   2016-12-02 10:23:20
* Last modified by:   WuLC
* Last Modified time: 2016-12-02 10:25:49
* Email: liangchaowu5@gmail.com
*/


// binary search
// use two binary search, one to find the insert position of target, another to find the insert position of target+1
// both insertion should maintain the nums in order, when there are duplicates, insert at the first position
public class Solution 
{
    public int[] searchRange(int[] nums, int target) 
    {
        int[] result = {-1, -1};
        if (nums.length == 0 || target < nums[0] || target > nums[nums.length-1]) return result;
        int leftInsertPoint = insertPosition(nums, target);
        int rightInsertPoint = insertPosition(nums, target + 1);
        if (rightInsertPoint != leftInsertPoint) 
        {
            result[0] = leftInsertPoint;
            result[1] = rightInsertPoint-1;
        }
        return result;
    }
    
    public int insertPosition(int[] nums, int target) // the first insert position of target to keep nums in order
    {
        int left = 0, right = nums.length-1, mid;
        while (left < right)
        {
            mid = left + ((right-left)>>1);
            if (nums[mid] >= target) right = mid;
            else left = mid + 1;
        }
        // left = right
        if (nums[left] >= target) return left;
        else return left + 1;
    }
}