/*
 * Created on Tue Jun 12 2018 11:54:48
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp
class Solution 
{
    public:
        double champagneTower(int poured, int query_row, int query_glass) 
        {
            vector<double> pre = {poured};
            for (int i=1; i <= query_row; i++)
            {
                vector<double> curr;
                for(int j=0; j<i+1; j++)
                {
                    double p = 0.0;
                    if(j != i) p += pre[j]>=1 ? (pre[j]-1)/2.0 : 0.0;
                    if(j != 0) p += pre[j-1]>=1 ? (pre[j-1]-1)/2.0 : 0.0;
                    curr.push_back(p);
                }
                pre = curr;
            }
            return pre[query_glass] > 1 ? 1.0 : pre[query_glass];
        }
};