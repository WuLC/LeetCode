/*
 * Created on Sat May 12 2018 19:58:31
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// simple dfs
class Solution 
{
    public:
        int numIslands(vector<vector<char>>& grid) 
        {
            if(grid.size() == 0) return 0;
            int count = 0;
            int m = grid.size(), n = grid[0].size();
            for(int i = 0; i < m; i++)
            {
                for(int j = 0; j < n; j++)
                {
                    if (grid[i][j] == '1')
                    {
                        count++;
                        dfs(grid, i, j, m, n);
                    }
                }
            }
            return count;
        }
        
        void dfs(vector<vector<char>>& grid, int i, int j, int m, int n)
        {
            if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1') return;
            grid[i][j] = '0';
            dfs(grid, i-1, j, m, n); 
            dfs(grid, i+1, j, m, n);
            dfs(grid, i, j-1, m, n);
            dfs(grid, i, j+1, m, n);
        }
};