/*
 * Created on Thu Jun 14 2018 18:17:23
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// naive dp without cache, TLE
class Solution 
{
    public:
        double soupServings(int N) 
        {
            return helper(N, N);
        }
        
        double helper(int A, int B)
        {
            if (A<=0 && B<=0) return 0.5;
            if (A<=0 && B>0) return 1;
            if (A>0 && B<=0) return 0;
            return 0.25*helper(A-100, B)+
                   0.25*helper(A-75, B-25)+ 
                   0.25*helper(A-50, B-50)+
                   0.25*helper(A-25, B-75);     
        }
};


// dp with cache, make 25ml as the smallest unit so as to reduce space
class Solution 
{
    private:
        double cache[200][200];
    
    public:
        double soupServings(int N) 
        {
            return N > 4800 ? 1 : helper(std::ceil(N/25.0), std::ceil(N/25.0));
        }
        
        double helper(int A, int B)
        {
            if (A<=0 && B<=0) return 0.5;
            if (A<=0 && B>0) return 1;
            if (A>0 && B<=0) return 0;
            if (cache[A][B] == 0)
                cache[A][B] = 0.25*helper(A-4, B) + 0.25*helper(A-3, B-1) + 0.25*helper(A-2, B-2) + 0.25*helper(A-1, B-3);     
            return cache[A][B];
        }
};