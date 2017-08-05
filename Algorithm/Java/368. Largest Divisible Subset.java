/*
* @Author: WuLC
* @Date:   2017-08-05 21:03:05
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-05 21:03:44
* @Email: liangchaowu5@gmail.com
*/

// dp
// time complexity: O(n^2) 
public class Solution 
{
    public List<Integer> largestDivisibleSubset(int[] nums) 
    {
        if(nums.length == 0) return new ArrayList<Integer>();
        Arrays.sort(nums);
        List<List<Integer>> record = new ArrayList<List<Integer>>();
        List<Integer> curr;
        int result = 0;
        for(int i = 0; i < nums.length; i++)
        {   
            int count = 0, idx = i;
            for(int j = 0; j < i; j++)
            {
                if (nums[i] % nums[j] == 0)
                {
                    if(record.get(j).size() > count)
                    {
                        count = record.get(j).size();
                        idx = j;
                    }
                }
            }
            if(idx != i) curr = new ArrayList<Integer>(record.get(idx));
            else curr = new ArrayList<Integer>();
            curr.add(nums[i]);
            record.add(curr);
            if (record.get(result).size() < curr.size()) result = i; 
        }
        return record.get(result);
    }
}