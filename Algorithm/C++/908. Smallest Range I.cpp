/*
 * Created on Sun Sep 23 2018 12:0:41
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
class Solution {
public:
    int smallestRangeI(vector<int>& A, int K) {
        int min=10000, max=0;
        for(int num:A){
            min=std::min(min, num);
            max=std::max(max, num);
        }

        if (K*2>=max-min){
            return 0;
        }
        else{
            return max-min-K*2;
        }
    }
};