/**
* Author: WuLC
* Date:   2017-04-30 10:38:51
* Last modified by:   WuLC
* Last Modified time: 2017-04-30 11:06:06
* Email: liangchaowu5@gmail.com
*/


// backtrack with dfs, pay attention to severl points
// 1. sort the array firstly, else test case like [4,4,4,1,4] will lead to duplicate
// 2. use set to store the result to avoid duplicate, then transfer it into list
// 3. traverse the possible number of elements in a subset
// 4. very slow solutioin, takes about 10ms
public class Solution
{
    private Set<List<Integer>> subSets;
    private List<Integer> tmp;
    
    public List<List<Integer>> subsetsWithDup(int[] nums)
    {
        subSets = new HashSet<List<Integer>>();
        tmp = new ArrayList<Integer>();
        Arrays.sort(nums);
        for(int k = 0; k <= nums.length; k++)
            dfs(k, 0, nums);
        // convert set into list    
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        result.addAll(subSets);
        return result;
    }
    
    public void dfs(int k, int idx, int[] nums)
    {
        if (tmp.size() == k)
        {
            subSets.add(new ArrayList<Integer>(tmp));
            return;
        }
        for(int i = idx; i < nums.length; i++)
        {
            tmp.add(nums[i]);
            dfs(k, i+1, nums);
            tmp.remove(tmp.size()-1);
        }
    }
}


// referer solution, still backtrack with dfs ,but much faster, take about 3 ms
// avoid duplicate results by avoiding adding duplicate numbers at each iteration

public class Solution 
{
    public List<List<Integer>> subsetsWithDup(int[] nums) 
    {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        dfs(nums, 0, new ArrayList<>(), res);
        return res;
    }
    
    private void dfs(int[] nums, int start, List<Integer> list, List<List<Integer>> res) 
    {
        res.add(new ArrayList<Integer>(list));
        for (int i = start; i < nums.length; i++) 
        {
            list.add(nums[i]);
            dfs(nums, i+1, list, res);
            list.remove(list.size()-1);
            while (i < nums.length - 1 && nums[i] == nums[i+1]) i++;
        }
    }
}