/*
* @Author: WuLC
* @Date:   2017-05-31 20:53:51
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-05 21:20:47
* @Email: liangchaowu5@gmail.com
*/


// naive dfs, TLE
public class Solution 
{
    private int result;
    private int[] visited;
    
    public int ladderLength(String beginWord, String endWord, List<String> wordList) 
    {
        result = 0;
        visited = new int[wordList.size()];
        dfs(beginWord, endWord, wordList, 1);
        return result;
    }
    
    
    public void dfs(String begin, String end, List<String> wordList, int count)
    {
        if (begin.equals(end))
        {
            if (result == 0) result = count;
            else result = Math.min(count, result);
            return;
        }
        
        for(int i = 0; i < wordList.size(); i++)
        {
            if (visited[i] == 0 && canTransform(begin, wordList.get(i))) 
            {
                visited[i] = 1;
                dfs(wordList.get(i), end, wordList,count+1);
                visited[i] = 0;
            }
        }
    }
    
    public boolean canTransform(String s1, String s2)
    {
        int count = 0;
        for(int i = 0; i < s1.length(); i++)
        {
            if ( s1.charAt(i) != s2.charAt(i) )
            {
                count++;
                if (count > 1) break;
            }
        }
        if (count == 1) return true;
        else return false;
    }
}



// bfs, start from 0 cells
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