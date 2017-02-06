/**
* Author: WuLC
* Date:   2017-02-06 16:44:32
* Last modified by:   WuLC
* Last Modified time: 2017-02-06 16:45:31
* Email: liangchaowu5@gmail.com
*/


// judge each edge of each cell
public class Solution 
{
    public int islandPerimeter(int[][] grid) 
    {
        if(grid.length == 0) return 0;
        int m = grid.length, n = grid[0].length, perimeter = 0;
        for(int i=0; i<m; i++)
        {
            for(int j = 0; j<n; j++)
            {
                if (grid[i][j] == 1)
                {
                    int tmp = 0;
                    if (i==0 || grid[i-1][j]==0) tmp++;
                    if (i==m-1 || grid[i+1][j]==0) tmp++;
                    if (j==0 || grid[i][j-1] == 0) tmp++;
                    if (j==n-1 || grid[i][j+1] == 0) tmp++;
                    perimeter += tmp;
                }
            }
        }
        return perimeter;
    }
}