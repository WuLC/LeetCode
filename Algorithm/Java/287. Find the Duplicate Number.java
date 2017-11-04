/*
 * Created on Sat Nov 04 2017 15:30:21
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// method 1, binary search 
// time O(nlogn), space O(1)
class Solution 
{
    public int findDuplicate(int[] nums) 
    {
        int left = 1, right = nums.length - 1;
        while(left < right)
        {
            int count = 0;
            int mid = left + ((right - left)>>1);
            for (int i = 0; i < nums.length; i++)
            {
                if(nums[i] <= mid)
                    count++;
            }
            if (count > mid) right = mid;
            else left = mid + 1;
        }
        return left;
    }
}

// method 2, two pointers
// there will always be a cycle among the numbers, and the duplicate number must be the entry of the cycle
// time complexity: O(n), space complexity: O(1)
class Solution 
{
    public int findDuplicate(int[] nums) 
    {
        int slow = nums[0];
        int fast = nums[nums[0]];
        while (slow != fast)
        {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        
        fast = 0;
        while(nums[fast] != nums[slow])
        {
            fast = nums[fast];
            slow = nums[slow];
        }
        return nums[fast];
    }
}