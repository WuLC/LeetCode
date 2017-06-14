/*
* @Author: WuLC
* @Date:   2017-06-10 17:23:34
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-10 17:24:18
* @Email: liangchaowu5@gmail.com
*/

// bfs, start from 0 cells
// and reach as many non-zero cells as possible
public class Solution 
{
    class Position
    {
        public int x;
        public int y;
        Position(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }
    
    public int[][] updateMatrix(int[][] matrix) 
    {
        int m = matrix.length, n = matrix[0].length;
        Queue<Position> queue = new LinkedList<Position>();
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (matrix[i][j] == 0) queue.add(new Position(i, j));
                else matrix[i][j] = -1;
            }
        }
        
        // dfs
        int distance = 1;
        int[][] directions = new int[][]{{-1,0}, {1,0}, {0,-1}, {0,1}};
        while(queue.size() > 0)
        {
           Queue<Position> next = new LinkedList<Position>();
           while(queue.size() > 0)
           {
               Position curr = queue.poll();
               for (int i = 0; i < 4; i++)
               {
                   int x = curr.x + directions[i][0];
                   int y = curr.y + directions[i][1];
                   // "matrix[x][y] == -1 || matrix[x][y] > distance" needs a bracket, otherwise it won't pass
                   if (x >= 0 && x < m && y >= 0 && y < n && (matrix[x][y] == -1 || matrix[x][y] > distance))
                   {
                       matrix[x][y] = distance;
                       next.add(new Position(x, y));
                   }
               }
           }
           queue = next;
           distance++;
        }
        return matrix;
    }
}