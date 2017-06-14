/*
* @Author: WuLC
* @Date:   2017-05-31 20:53:51
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-10 17:21:33
* @Email: liangchaowu5@gmail.com
*/


// naive dfs, TLE
public class Solution 
{
    private int result;
    private int[] visited;
    
    public int ladderLength(String beginWord, String endWord, List<String> wordList) 
    {
        result = 0;
        visited = new int[wordList.size()];
        dfs(beginWord, endWord, wordList, 1);
        return result;
    }
    
    
    public void dfs(String begin, String end, List<String> wordList, int count)
    {
        if (begin.equals(end))
        {
            if (result == 0) result = count;
            else result = Math.min(count, result);
            return;
        }
        
        for(int i = 0; i < wordList.size(); i++)
        {
            if (visited[i] == 0 && canTransform(begin, wordList.get(i))) 
            {
                visited[i] = 1;
                dfs(wordList.get(i), end, wordList,count+1);
                visited[i] = 0;
            }
        }
    }
    
    public boolean canTransform(String s1, String s2)
    {
        int count = 0;
        for(int i = 0; i < s1.length(); i++)
        {
            if ( s1.charAt(i) != s2.charAt(i) )
            {
                count++;
                if (count > 1) break;
            }
        }
        if (count == 1) return true;
        else return false;
    }
}