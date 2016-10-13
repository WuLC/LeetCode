/**
* Author: WuLC
* Date:   2016-10-13 07:59:15
* Last modified by:   WuLC
* Last Modified time: 2016-10-13 13:33:49
* Email: liangchaowu5@gmail.com
*/

//the main idea is backtracking, but the way of detecting conflict can be optimized
// use a one-demensional array to store the positions of queen of each row instead of a two-dementional array representing the graph

// method 1
// detect confilct of the current position row by row, O(n) time for each detect 
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


// method 2 
// use three arrays to detect the conflict of the current position in column , left-cross-line, righ-cross-line, O(1) time
public class Solution 
{
    public int[] column;
    public int[] left_cross;
    public int[] right_cross;
    public int[] positions;
    public List<List<String>> result;
    
    
    public List<List<String>> solveNQueens(int n) 
    {
        column = new int[n];
        left_cross = new int[2*n-1];
        right_cross = new int[2*n-1];
        positions = new int[n];
        result = new ArrayList<List<String>>();
        dfs(0, n);
        return result;
    }
    
    public void dfs(int row, int n)
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
            if (column[col] == 1 || left_cross[row+col]==1 || right_cross[n-1-row+col] == 1)
                continue;
            else
                {
                    column[col] = 1; left_cross[row+col]=1; right_cross[n-1-row+col] = 1;
                    positions[row] = col;
                    dfs(row + 1, n);
                    column[col] = 0; left_cross[row+col]=0; right_cross[n-1-row+col] = 0;
                }
        }
    }
}