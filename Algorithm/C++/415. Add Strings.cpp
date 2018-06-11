/*
 * Created on Mon Jun 11 2018 20:27:44
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// simple solution
class Solution 
{
    public:
        string addStrings(string num1, string num2) 
        {
            int carry = 0;
            int idx1 = num1.length()-1, idx2 = num2.length() - 1;
            string result = "";
            while(idx1 >=0 || idx2 >= 0)
            {
                int sum = carry;
                if (idx1 >= 0) 
                {
                    sum += num1[idx1] - '0';
                    idx1 -= 1;
                }
                if (idx2 >= 0) 
                {
                    sum += num2[idx2] - '0';
                    idx2 -= 1;
                }
                carry = sum/10;
                result = std::to_string(sum%10) + result;
            }
            if (carry) result = "1"+result;
            return result;
        }
};