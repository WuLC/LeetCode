/*
* @Author: WuLC
* @Date:   2017-06-29 12:58:24
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-29 12:59:28
* @Email: liangchaowu5@gmail.com
*/


// two choices, choose to exclude the first house or th last house
public class Solution 
{
    public int rob(int[] nums) 
    {
        if(nums.length == 0) return 0;
        else if(nums.length == 1) return nums[0];
        else if(nums.length == 2) return Math.max(nums[0], nums[1]);
        else return Math.max(helper(nums, 0, nums.length -2), helper(nums, 1, nums.length - 1));
    }
    
    public int helper(int[] nums, int start, int end)
    {
        int pre1 = nums[start], pre2 = Math.max(nums[start], nums[start+1]);
        int index = start + 2, curr = pre2;
        while(index <= end)
        {
            curr = Math.max(pre2, pre1 + nums[index]);
            pre1 = pre2;
            pre2 = curr;
            index++;
        }
        return curr;
    }
}