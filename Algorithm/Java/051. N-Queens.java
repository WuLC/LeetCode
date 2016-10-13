/**
* Author: WuLC
* Date:   2016-10-13 07:59:15
* Last modified by:   WuLC
* Last Modified time: 2016-10-13 08:01:17
* Email: liangchaowu5@gmail.com
*/


// method 1
// backtracking
// use an array to store the positions of queen of each row
public class Solution 
{
    
    public List<List<String>> solveNQueens(int n) 
    {
        List<List<String>> result = new ArrayList<List<String>>();
        int[] positions = new int[n];
        dfs(0, n, positions, result);
        return result;
    }
    
    public void dfs(int row, int n, int[] positions, List<List<String>> result)
    {
        if (row == n)
        {
            List<String> tmp = new ArrayList<String>();
            char[] pos = new char[n];
            Arrays.fill(pos, '.');
            for (int i = 0; i < n; i++)
            {
                pos[positions[i]] = 'Q';
                tmp.add(new String(pos));
                pos[positions[i]] = '.';
            }
            result.add(tmp);
            return ;
        }
        for (int col=0; col < n; col ++)
        {   
            boolean ok = true;
            for (int i=0; i < row; i++)
            {
                if (col == positions[i] || col - positions[i] == row - i || positions[i] - col == row - i)
                {
                    ok = false;
                    break;
                }
            }  
            if (ok)
            {
                positions[row] = col;
                dfs(row + 1, n, positions, result);
            }
        }
    }
}