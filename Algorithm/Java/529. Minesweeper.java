/**
* Author: WuLC
* Date:   2017-05-24 17:54:53
* Last modified by:   WuLC
* Last Modified time: 2017-05-24 17:55:19
* Email: liangchaowu5@gmail.com
*/


// dfs
public class Solution 
{
    public char[][] updateBoard(char[][] board, int[] click) 
    {
        int r = click[0], c = click[1];
        if (board[r][c] == 'M') board[r][c] = 'X';
        else dfs(board, r, c, board.length, board[0].length);
        return board;
    }
    
    public void dfs(char[][] board, int r, int c, int m, int n)
    {
        int count = 0;
        for(int i=-1; i<=1; i++)
            for(int j=-1; j<=1; j++)
                if ( r+i >= 0 && r+i < m && c+j >= 0 && c+j < n && board[r+i][c+j] == 'M')  count += 1;
        if (count != 0) board[r][c] = (char)(count+'0'); // convert digit to char, char() return the corresponing ASCII character
        else
        {
            board[r][c] = 'B';
            for(int i=-1; i<=1; i++)
                for(int j=-1; j<=1; j++)
                    if ( r+i >= 0 && r+i < m && c+j >= 0 && c+j < n && board[r+i][c+j] == 'E') dfs(board, r+i, c+j, m, n);
        }
    }
}

// bfs