/**
* Author: WuLC
* Date:   2016-12-03 21:18:47
* Last modified by:   WuLC
* Last Modified time: 2016-12-03 21:24:42
* Email: liangchaowu5@gmail.com
*/

// bit manipulation and backtracking
public class Solution 
{
    private int[] row;
    private int[] col;
    private int[][] block;
    
    public void solveSudoku(char[][] board) 
    {
        row = new int[9];
        col = new int[9];
        block = new int[3][3];
        int num;
        // init row, col and block
        for(int i=0; i<9; i++)
        {
            for (int j=0; j<9; j++)
            {
                if (board[i][j]  == '.') continue;
                num = board[i][j] - '0';
                row[i] ^= (1<<num);
                col[j] ^= (1<<num);
                block[i/3][j/3] ^= (1<<num);
            }
        }
        dfs(board, 0, 0);
    }
    
    public boolean dfs(char[][] board, int r, int c)
    {
        if (c == 9) r += 1;
        for(int i=r; i<9; i++)
        {
            for(int j=0; j<9; j++)
            {
                if (board[i][j] != '.') continue;
                for (int num=1; num<10; num++)
                {
                    int tmp = (1<<num);
                    if ( (row[i]&tmp)==0 && (col[j]&tmp)==0 && (block[i/3][j/3]&tmp) == 0)
                    {
                        row[i] ^= tmp;
                        col[j] ^= tmp;
                        block[i/3][j/3] ^= tmp;
                        board[i][j] = (char)(num+48);
                        if (dfs(board, i, j+1)) return true;
                        else
                        {
                            row[i] ^= tmp;
                            col[j] ^= tmp;
                            block[i/3][j/3] ^= tmp;
                            board[i][j] = '.';
                        }
                    }
                }
                return false; // can not fill in a correct number for the current position
            }
        }
        return true;
    }
}