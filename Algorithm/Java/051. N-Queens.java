/**
* Author: WuLC
* Date:   2016-10-13 07:59:15
* Last modified by:   WuLC
* Last Modified time: 2016-10-14 15:53:45
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

// method 3
// same idea as method 2, but use the bits of a long number to replace the arrays in method 2(Bit manipulation)
// thus there is a max limit to n, that is 32,cause 64 > (2*32 - 1)
public class Solution 
{
    public long column;
    public long left_cross;
    public long right_cross;
    public int[] positions;
    public List<List<String>> result;
      
    public List<List<String>> solveNQueens(int n) 
    {
        column = 0;
        left_cross = 0;
        right_cross = 0;
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
        long one = 1;
        for (int col=0; col < n; col ++)
        {   
            if ( (column&(one<<col))!=0 || (left_cross&(one<<(row+col)))!= 0 || (right_cross&(one<<(n-1-row+col)))!=0)
                continue;
            else
                {
                    column ^= (one<<col); left_cross ^= (one<<(row+col)); right_cross ^= (one<<(n-1-row+col));
                    positions[row] = col;
                    dfs(row + 1, n);
                    column ^= (one<<col); left_cross ^= (one<<(row+col)); right_cross ^= (one<<(n-1-row+col));
                }
        }
    }
}


// method 4
// with bit manipulation, use lowbit to locate directly which positions cause no conflict
// there is still the maximal limit for n (n<=32) since there is only 64 bits for the long type
public class Solution 
{
    public long column;
    public long left_cross;
    public long right_cross;
    public int[] positions;
    public List<List<String>> result;
    
    public List<List<String>> solveNQueens(int n) 
    {
        column = 0;
        left_cross = 0;
        right_cross = 0;
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
        long one = 1;
        // find the positions of columns for the current row, make the possible positions 1 and impossible positions 0
        long available =  ((one<<n)-1) & ~(column | (left_cross>>row) | (right_cross >> (n-1-row)));
        long lowBit, tmp;
        int count;
        while (available != 0)
        {
            count = 0;
            lowBit = tmp =  available & -available;
            available ^= lowBit;
            while (tmp > 0)
            {
                tmp >>= 1;
                count += 1;
            } 
            positions[row] = count-1;
            column ^= lowBit; left_cross ^= (lowBit<<row); right_cross ^= (lowBit<<(n-1-row));
            dfs(row+1, n);
            column ^= lowBit; left_cross ^= (lowBit<<row); right_cross ^= (lowBit<<(n-1-row));
        }
    }
}