/**
* Author: LC
* Date:   2016-10-26 09:17:15
* Last modified by:   WuLC
* Last Modified time: 2016-10-26 09:23:57
* Email: liangchaowu5@gmail.com
*/


// add left bracket when the number of left bracket is smaller than n
// add right bracket when the number of right bracket is  smaller than the number of left bracket
public class Solution 
{
    private List<String> result = new ArrayList<String>();
    public List<String> generateParenthesis(int n) 
    {
        helper(0, 0, n, "");
        return result;
    }
    
    private void helper(int left, int right, int n, String tmp)
    {
        if (left==n && right==n) result.add(tmp);
        if (left < n) helper(left + 1, right, n, tmp+'(');
        if (left > right) helper(left, right+1, n, tmp+')');
    }
}