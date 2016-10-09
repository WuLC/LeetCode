/**
* Author: WuLC
* Date:   2016-10-09 19:08:33
* Last modified by:   WuLC
* Last Modified time: 2016-10-09 19:18:59
* Email: liangchaowu5@gmail.com
*/

/*
O(n) space, O(n) time
use Hash table to store index of nums 
*/

public class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i=0; i < nums.length; i++)
        {
            if (map.containsKey(target - nums[i]))
            {
                return new int[] {map.get(target - nums[i]), i};
            }
            map.put(nums[i], i);
        }
        return null;
        
    }
}

