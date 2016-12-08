/**
* Author: WuLC
* Date:   2016-12-08 18:53:37
* Last modified by:   WuLC
* Last Modified time: 2016-12-08 18:53:56
* Email: liangchaowu5@gmail.com
*/


// backtracking
public class Solution 
{
    private ArrayList<List<Integer>> result;  
    public List<List<Integer>> combinationSum(int[] candidates, int target) 
    {
        result = new ArrayList<List<Integer>>();
        List<Integer> tmp = new ArrayList<Integer>();
        Arrays.sort(candidates);
        dfs(candidates, tmp, 0, 0, target);
        return result;
    }
    
    public void dfs(int[] candidates, List<Integer> tmp, int idx, int count, int target)
    {
        if (count == target)
        {
            result.add(new ArrayList(tmp));
            return ;
        }
        
        for (int i=idx; i < candidates.length; i++)
        {
            if (count+candidates[i] <= target)
            {
                tmp.add(candidates[i]);
                dfs(candidates, tmp, i, count+candidates[i], target);
                tmp.remove(tmp.size()-1);
            }
            else return;
        }
    }
}