/*
 * Created on Tue May 01 2018 22:37:15
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// how to convert int to string in cpp
class Solution {
    public:
        vector<string> fizzBuzz(int n)
        {
            std::vector<string> result;
            for(int i=1; i<=n; i++)
            {
                string tmp="";
                if(i%3==0) tmp += "Fizz";
                if(i%5==0) tmp += "Buzz";
                if(tmp.size()==0) tmp += std::to_string(i);
                result.push_back(tmp);
            }
            return result;
        }
};