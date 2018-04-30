/*
 * Created on Mon Apr 30 2018 9:48:16
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dfs, pay attention to the case when old color == new color 
class Solution 
{
    public:
        vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) 
        {
            if(newColor != image[sr][sc])
               dfs(image, sr, sc, newColor, image[sr][sc]);
           return image;
        }
    
        void dfs(vector<vector<int>>& image, int sr, int sc, int newColor, int oldColor)
        {
            if (sr < 0 || sr >= image.size() || sc < 0 || sc >= image[0].size()) return;
            if (image[sr][sc] == oldColor)
            {
                image[sr][sc] = newColor;
                dfs(image, sr-1, sc, newColor, oldColor);
                dfs(image, sr+1, sc, newColor, oldColor);
                dfs(image, sr, sc-1, newColor, oldColor);
                dfs(image, sr, sc+1, newColor, oldColor);
            }
            return;
        }
};