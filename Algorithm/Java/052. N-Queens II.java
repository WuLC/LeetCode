/**
* Author: WuLC
* Date:   2016-12-27 23:22:58
* Last modified by:   WuLC
* Last Modified time: 2016-12-28 00:18:33
* Email: liangchaowu5@gmail.com
*/


// method 1, dfs
// with bit manipulation instead of boolean array to judge collision
public class Solution 
{
    private int result, column, leftBias, rightBias;
    public int totalNQueens(int n) 
    {
        result = column = leftBias = rightBias = 0;
        dfs(0, n);
        return result;
    }
    
    public void dfs(int row, int n)
    {
        if (row == n)
        {
            result += 1;
            return;
        }
        for(int col = 0; col < n; col++)
        {
            if ((column&(1<<col)) == 0 && (leftBias&(1<<(row+col))) == 0 && (rightBias&(1<<(row-col+n-1))) == 0)
            {
                column ^= (1<<col); leftBias ^= (1<<(row+col)); rightBias ^= (1<<(row-col+n-1));
                dfs(row+1,n);
                column ^= (1<<col); leftBias ^= (1<<(row+col)); rightBias ^= (1<<(row-col+n-1));
            }
        }
        
    }
}


// method 2, dfs
// base on method 1, find the valid positions for each row instead of traverse and judge one by one
public class Solution 
{
    private int result, column, leftBias, rightBias;
    public int totalNQueens(int n) 
    {
        result = column = leftBias = rightBias = 0;
        dfs(0, n);
        return result;
    }
    
    public void dfs(int row, int n)
    {
        if (row == n)
        {
            result += 1;
            return;
        }
        int validPosition =  (~(column | (leftBias >> row) | (rightBias >> (n-row-1)))) & ((1<<n)-1);
        while (validPosition != 0)
        {   
            int col = validPosition&(-validPosition); // low bit 
            validPosition ^= col;
            column ^= col; leftBias ^= (col << row) ; rightBias ^= (col << (n - row-1));
            dfs(row+1,n);
            column ^= col; leftBias ^= (col << row) ; rightBias ^= (col << (n - row-1));
        }
    }
}


