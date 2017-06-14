/*
* @Author: WuLC
* @Date:   2017-06-14 14:40:39
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-14 14:43:25
* @Email: liangchaowu5@gmail.com
*/


// Hashmap
public class Solution 
{
    public boolean checkSubarraySum(int[] nums, int k) 
    {
        Map<Integer, Integer> indices = new HashMap<Integer, Integer>();
        indices.put(0, -1);
        int currSum = 0, tmp;
        for (int i = 0; i < nums.length; i++)
        {
            currSum += nums[i];
            if (k != 0) tmp = currSum % k;
            else tmp = currSum;
            if (indices.containsKey(tmp))
            {
                if (i - indices.get(tmp) > 1) return true;
            }
            else indices.put(tmp, i);
        }
        return false;
    }
}

// same as above , but a little more concise
public class Solution 
{
    public boolean checkSubarraySum(int[] nums, int k) 
    {
        Map<Integer, Integer> indices = new HashMap<Integer, Integer>();
        indices.put(0, -1);
        int currSum = 0;
        for (int i = 0; i < nums.length; i++)
        {
            currSum += nums[i];
            if (k != 0) currSum = currSum % k;
            if (indices.containsKey(currSum))
            {
                if (i - indices.get(currSum) > 1) return true;
            }
            else indices.put(currSum, i);
        }
        return false;
    }
}