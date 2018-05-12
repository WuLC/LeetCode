/*
 * Created on Sat May 12 2018 19:50:30
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple dfs
class Solution 
{
    public:
        int maxAreaOfIsland(vector<vector<int>>& grid) 
        {
            if(grid.size() == 0) return 0;
            int result = 0;
            int m = grid.size(), n = grid[0].size();
            for(int i = 0; i < m; i++)
            {
                for(int j = 0; j < n; j++)
                {
                    if (grid[i][j] == 1)
                        result = std::max(result, dfs(grid, i, j, m, n));
                }
            }
            return result;
        }
        
        int dfs(vector<vector<int>>& grid, int i, int j, int m, int n)
        {
            if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != 1) return 0;
            grid[i][j] = -1;
            return 1 + dfs(grid, i-1, j, m, n) + dfs(grid, i+1, j, m, n) + dfs(grid, i, j-1, m, n) + dfs(grid, i, j+1, m, n);
        }
};