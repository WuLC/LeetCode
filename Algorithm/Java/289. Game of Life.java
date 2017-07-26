/**
* Author: LC
* Date:   2017-07-27 00:34:29
* Last modified by:   LC
* Last Modified time: 2017-07-27 00:35:53
* Email: liangchaowu5@gmail.com
*/


// define a new class to represent the position that need to change 
public class Solution 
{
    
    private class Position
    {
        public int x;
        public int y;
        Position(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }
    
    public void gameOfLife(int[][] board) 
    {
        if(board.length == 0) return;
        List<Position> change = new ArrayList<Position>();
        int m = board.length, n = board[0].length;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                int count = 0;
                for(int p = -1; p <= 1; p++)
                {
                    for(int q = -1; q <= 1; q++)
                    {
                        if (p == 0 && q == 0) continue;
                        if (i + p >= 0 && i + p < m && j + q >= 0 && j + q < n && board[i+p][j+q] == 1) count++;
                    }
                }
                if(board[i][j] == 1 && (count < 2 || count > 3)) change.add(new Position(i,j));
                if(board[i][j] == 0 && count == 3) change.add(new Position(i, j));
            }
        }
        Position tmp;
        for(int i = 0; i < change.size(); i++)
        {
            tmp = change.get(i);
            board[tmp.x][tmp.y] ^= 1;
        }
        return;
    }
}