#include <vector>
#include <string>

class Solution {
public:
    int longestPalindrome(std::string s, std::string t) {
        std::reverse(t.begin(), t.end());
        int m = s.size(), n = t.size(), result = 1;

        std::vector<int> s_pal(m, 1), t_pal(n, 1);
        longestPalindromeStarted(s, s_pal);
        longestPalindromeStarted(t, t_pal);

        std::vector<std::vector<int>> dp(m+1, std::vector<int>(n+1, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (s[i] == t[j]) {
                    dp[i+1][j+1] = std::max(dp[i+1][j+1], dp[i][j]+1);
                }
                int tmp = dp[i+1][j+1]*2;
                if (tmp == 0) {
                    tmp = std::max(s_pal[i], t_pal[j]);
                } else {
                    if (i+1 < m && j+1 < n) {
                        tmp += std::max(s_pal[i+1], t_pal[j+1]);
                    } else if (i+1 < m) {
                        tmp += s_pal[i+1];
                    } else if (j+1 < n) {
                        tmp += t_pal[j+1];
                    }
                }
                result = std::max(result, tmp);
            }
        }
        return result;
    }

    void longestPalindromeStarted(std::string& s, std::vector<int>& s_pal) {
        int n = s.size(), l, r;
        for (int i = 0; i < n; i++) {
            for (int j = n-1; j > i; j--) {
                l = i, r = j;
                while (l < r && s[l] == s[r]) {
                    l++, r--;
                }
                if (l >= r) {
                    s_pal[i] = j-i+1;
                    break;
                }
            }
        }
        return;
    }
};