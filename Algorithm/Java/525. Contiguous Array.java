/*
* @Author: WuLC
* @Date:   2017-08-05 12:37:44
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-05 12:38:01
* @Email: liangchaowu5@gmail.com
*/

// change 0 to -1 and use hashmap
public class Solution
{
    public int findMaxLength(int[] nums) 
    {
        int curr_sum = 0;
        int result = 0;
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        count.put(0, -1);
        for(int i = 0; i < nums.length; i++)
        {
            if(nums[i] == 0) nums[i] = -1;
            curr_sum += nums[i];
            if(count.containsKey(curr_sum)) result = Math.max(result, i - count.get(curr_sum));
            else count.put(curr_sum, i);    
        }
        return result;
    }
}