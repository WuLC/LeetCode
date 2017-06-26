/*
* @Author: WuLC
* @Date:   2017-06-26 13:35:10
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-26 13:36:15
* @Email: liangchaowu5@gmail.com
*/

// sort and assign
public class Solution 
{
    public int findContentChildren(int[] g, int[] s) 
    {
        Arrays.sort(g);
        Arrays.sort(s);
        int i = 0, j = 0, count = 0;
        while (j < s.length && i < g.length)
        {
            if (s[j] >= g[i])
            {
                i++;
                count++;
            }
            j++;
        }
        return count;
    }
}                                                                             