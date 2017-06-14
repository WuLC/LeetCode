/*
* @Author: WuLC
* @Date:   2017-06-14 15:51:13
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-14 15:51:23
* @Email: liangchaowu5@gmail.com
*/


// hashmap
public class Solution
{
    public int subarraySum(int[] nums, int k) 
    {
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        count.put(0, 1);
        int currSum = 0, result = 0;
        for (int num : nums)
        {
            currSum += num;
            if (count.containsKey(currSum - k)) result += count.get(currSum - k);
            if (count.containsKey(currSum)) count.put(currSum, count.get(currSum) + 1);
            else count.put(currSum, 1);
        }
        return result;
    }
}