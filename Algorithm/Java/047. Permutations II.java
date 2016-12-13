/**
* Author: WuLC
* Date:   2016-12-13 21:06:33
* Last modified by:   WuLC
* Last Modified time: 2016-12-13 21:07:42
* Email: liangchaowu5@gmail.com
*/


// recursive, same idea as 46. Permutations, but use a set to avoid duplicate number to be moved to the first place
public class Solution {
    
    private List<List<Integer>> result;
    public List<List<Integer>> permuteUnique(int[] nums) 
    {
        result = new ArrayList<List<Integer>>();
        dfs(nums, 0);
        return result;
    }
    
    public void dfs(int[] nums, int idx)
    {
        if (idx == nums.length)
        {
            List<Integer> tmp = new ArrayList<Integer>();
            for (int num:nums) tmp.add(num);
            result.add(tmp);
            return;
        }
        Set<Integer> appear = new HashSet<Integer>();
        for(int i=idx; i < nums.length; i++)
        {
            if (!appear.contains(nums[i]))
            {
                appear.add(nums[i]);
                swap(nums, idx, i);
                dfs(nums, idx+1);
                swap(nums, idx, i);
            }
        }
    }
    
    public void swap(int[] nums, int i, int j)
    {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}