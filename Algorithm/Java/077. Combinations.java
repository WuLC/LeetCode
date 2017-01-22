/**
* Author: WuLC
* Date:   2017-01-22 21:19:50
* Last modified by:   WuLC
* Last Modified time: 2017-01-22 21:20:08
* Email: liangchaowu5@gmail.com
*/

// dfs
public class Solution 
{
    private List<List<Integer>> result;
    private List<Integer> tmp;
    public List<List<Integer>> combine(int n, int k) 
    {
        result = new ArrayList<List<Integer>>();
        tmp = new ArrayList<Integer>();
        dfs(1, n, k);
        return result;
    }
    
    private void dfs(int curr, int n, int k)
    {
        if (tmp.size() == k)
        {
            result.add(new ArrayList(tmp));
            return;
        }
        for(int i=curr; i<=n; i++)
        {
            tmp.add(i);
            dfs(i+1, n, k);
            tmp.remove(tmp.size()-1);
        }
    }
}