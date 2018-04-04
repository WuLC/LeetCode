/*
 * Created on Thu Apr 05 2018 0:11:57
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

class Solution 
{
    public boolean exist(char[][] board, String word) 
    {
        char[] w = word.toCharArray();
        for (int i=0; i<board.length; i++)
        {
            for(int j=0; j<board[i].length; j++)
            {
                if (board[i][j] == w[0] && dfs(board, i, j, w, 0))
                    return true;
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, int i, int j, char[] w, int idx)
    {
        if (idx == w.length) return true;
        if (i < 0 || i >= board.length || j < 0 || j >= board[i].length || w[idx] != board[i][j]) return false;
        char tmp = board[i][j];
        board[i][j] = '.';
        if (dfs(board, i+1, j, w, idx+1) || 
            dfs(board, i-1, j, w, idx+1) || 
            dfs(board, i, j-1, w, idx+1) ||
            dfs(board, i, j+1, w, idx+1))
            return true;
        board[i][j] = tmp;
        return false;
    }
}