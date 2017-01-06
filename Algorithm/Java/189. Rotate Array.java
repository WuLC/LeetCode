/**
* Author: WuLC
* Date:   2017-01-06 17:41:28
* Last modified by:   WuLC
* Last Modified time: 2017-01-06 21:34:55
* Email: liangchaowu5@gmail.com
*/


//method 1, use another array to store the new number array
//O(n) time, O(n) space
public class Solution 
{
    public void rotate(int[] nums, int k) 
    {
        if(nums.length ==0 || k%nums.length == 0) return;
        int n = nums.length;
        int[] newNums = new int[n];
        for(int i=0; i<n; i++) newNums[(i+k)%n] = nums[i];
        for(int i=0; i<n; i++) nums[i] = newNums[i];
    }
}