// char 与 int 的预算，默认会转为 int，需要通过 static_cast<char> 来转换为 char
// char 没法转换为 string，需要通过 string 构造函数或 str += char 来拼接
#include <string>
#include <vector>

class Solution {
public:
    std::string smallestPalindrome(std::string s) {
        std::vector<int> counter(26, 0);
        for (char c : s) {
            counter[c-'a']++;
        }

        std::string mid="", left="", right="";
        for (int i = 0; i < counter.size(); i++) {
            if (counter[i] > 0) {
                if ((counter[i]&1) > 0) {
                    mid = std::string{static_cast<char>('a'+i)};
                }
                std::string tmp(counter[i]>>1, static_cast<char>('a'+i));
                left += tmp;
                right = tmp + right;
            }
        }
        return left+mid+right;
    }
};