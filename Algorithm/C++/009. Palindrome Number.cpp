/*
 * Created on Thu Apr 19 2018 14:41:13
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// method 1, convert number to string
class Solution 
{
    public:
        bool isPalindrome(int x) 
        {
            string s = std::to_string(x);
            int left = 0, right = s.length()-1;
            while(left < right)
            {
                if (s[left] != s[right])
                    return false;
                left++;
                right--;
            }
            return true;
        }
};

// method 2,no need to convert number to string
// follow the method of reversing a number
class Solution {
    public:
        bool isPalindrome(int x) 
        {
            if (x<0 || (x>0 && x%10==0)) return false;
            int sum = 0;
            while(x>sum)
            {
                sum = sum*10+x%10;
                x/=10;
            }
            return x==sum || x==sum/10;
        }
};