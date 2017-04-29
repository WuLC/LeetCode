/**
* Author: WuLC
* Date:   2017-04-29 10:33:55
* Last modified by:   WuLC
* Last Modified time: 2017-04-29 10:35:23
* Email: liangchaowu5@gmail.com
*/


// backtrack with dfs
public class Solution 
{
    private List<List<String>> result;
    private List<String> tmp;
    
    public List<List<String>> partition(String s) 
    {
        result = new ArrayList<List<String>>();
        tmp = new ArrayList<String>();
        dfs(0, s);
        return result;
    }
    
    public void dfs(int idx, String s)
    {
        if(idx == s.length()) 
        {
            result.add(new ArrayList(tmp));
            return;
        }
        String ts = "";
        for(int i=idx; i < s.length(); i++)
        {
            ts += s.charAt(i);
            if (isPalindrome(ts))
            {
                tmp.add(ts);
                dfs(i+1, s);
                tmp.remove(tmp.size()-1);
            }
        }
    }
    
    public boolean isPalindrome(String s)
    {
        int n = s.length();
        for(int i=0; i < (n>>1) ;i++)
            if(s.charAt(i) != s.charAt(n-i-1))
                return false;
        return true;
    }
}