/**
* Author: WuLC
* Date:   2016-12-13 20:54:34
* Last modified by:   WuLC
* Last Modified time: 2016-12-13 21:02:24
* Email: liangchaowu5@gmail.com
*/


// recursive, take each distinct number as the first number and permutate the rest
public class Solution 
{
    private List<List<Integer>> result;
    public List<List<Integer>> permute(int[] nums) 
    {
        result = new ArrayList<List<Integer>>();
        dfs(nums, 0);
        return result;
    }
    
    public void dfs(int[] nums, int idx)
    {
        if (idx == nums.length)
        {
            //List<Integer> tmp = new ArrayList<Integer>(Arrays.asList(nums));
            // the above line doesn't work
            List<Integer> tmp = new ArrayList<Integer>();
            for (int num:nums) tmp.add(num);
            result.add(tmp);
            return;
        }
        for(int i=idx; i < nums.length; i++)
        {
            swap(nums, idx, i);
            dfs(nums, idx+1);
            swap(nums, idx, i);
        }
    }
    
    public void swap(int[] nums, int i, int j)
    {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}