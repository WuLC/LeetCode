/**
* Author: WuLC
* Date:   2017-04-28 11:14:21
* Last modified by:   WuLC
* Last Modified time: 2017-04-28 11:16:11
* Email: liangchaowu5@gmail.com
*/

// backtrack with dfs, need to pay attention:
// 1. illegal long string will lead to TLE
// 2. 0 is legal but 01 is not
// 3. ip need to have 4 blocks, use String.join('.', List) to construct the ip address

public class Solution 
{
    private List<String> ips, tmp;
    public List<String> restoreIpAddresses(String s) 
    {        
        ips = new ArrayList<String>();
        tmp = new ArrayList<String>();
        if (s.length() > 12) return ips; // illegal long string will lead to TLE
        dfs(0, s);
        return ips;
    }
    
    public void dfs(int idx, String s)
    {
        if (idx == s.length())
        {
            if (tmp.size() ==4) ips.add(String.join(".", tmp));
            return;
        }
        String block = "";
        for (int i=idx; i < s.length(); i++)
        {
            block += s.charAt(i);
            if (block.length() > 1 && block.charAt(0) == '0') return; // 01 is not legal
            if (Integer.valueOf(block) <= 255)
            {
                tmp.add(block);
                dfs(i+1, s);
                tmp.remove(tmp.size()-1);
            }
            else return;
        }
    }
}