/**
* Author: LC
* Date:   2017-01-25 14:38:20
* Last modified by:   WuLC
* Last Modified time: 2017-01-25 14:38:34
* Email: liangchaowu5@gmail.com
*/


// dfs
public class Solution 
{
    private List<List<Integer>> result;
    private List<Integer> tmp;
    
    public List<List<Integer>> subsets(int[] nums) 
    {
        result = new ArrayList<List<Integer>>();
        tmp = new ArrayList<Integer>();
        for(int i=0; i<= nums.length; i++) dfs(0, i, nums);
        return result;
    }
    
    public void dfs(int idx, int k, int[] nums)
    {
        if (tmp.size() == k)
        {
            result.add(new ArrayList(tmp));
            return;
        }
        for (int i=idx; i<nums.length; i++)
        {
            tmp.add(nums[i]);
            dfs(i+1, k, nums);
            tmp.remove(tmp.size() - 1);
        }
    }
}