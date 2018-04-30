/*
 * Created on Mon Apr 30 2018 11:35:19
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// count the number of valid edges for each island
class Solution 
{
    public:
        int islandPerimeter(vector<vector<int>>& grid) 
        {
            int count = 0;
            int m = grid.size(), n = grid[0].size();
            for(int i=0; i<m; i++)
            {
                for(int j=0; j<n; j++)
                {
                    if (grid[i][j] == 1)
                    {
                        int tmp=4;
                        if(i-1>=0 && grid[i-1][j]==1) tmp--;
                        if(i+1<m && grid[i+1][j]==1) tmp--;
                        if(j-1>=0 && grid[i][j-1]==1) tmp--;
                        if(j+1<n && grid[i][j+1]==1) tmp--;
                        count += tmp;
                    }
                }
            }
            return count;
        }
};