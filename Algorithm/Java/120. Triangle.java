/*
 * Created on Sat Mar 31 2018 20:40:15
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp, O(n) space, from bottom to top
class Solution 
{
    public int minimumTotal(List<List<Integer>> triangle) 
    {
        int n = triangle.size();
        if (n == 0) return 0;
        int[] curr = new int[n];
        for(int i=n-1; i>=0; i--)
        {
            for(int j=0; j<triangle.get(i).size(); j++)
            {
                if(i==n-1) curr[j] = triangle.get(i).get(j);
                else curr[j] = Math.min(curr[j], curr[j+1]) + triangle.get(i).get(j);
            }
        }
        return curr[0];
    }
}