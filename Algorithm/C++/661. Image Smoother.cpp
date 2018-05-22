/*
 * Created on Tue May 22 2018 21:14:22
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
class Solution 
{
    public:
        vector<vector<int>> imageSmoother(vector<vector<int>>& M) 
        {
            vector<vector<int>> result;
            if (M.size() == 0) return result;
            int m = M.size(), n = M[0].size();
            for(int i=0; i<m; i++)
            {
                vector<int> tmp;
                for(int j=0; j<n; j++)
                {
                    int sum=0, count = 0;
                    for (int r=-1; r<=1; r++)
                        for(int c=-1; c<=1; c++)
                            if(i+r >= 0 && i+r < m && j+c >= 0 && j+c < n)
                            {
                                count++;
                                sum += M[i+r][j+c];
                            }
                                
                    tmp.push_back(std::floor(sum/count));
                }
                result.push_back(tmp);
            }
            return result;
        }
};