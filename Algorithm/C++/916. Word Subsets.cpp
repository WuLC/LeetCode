/*
 * Created on Wed Oct 03 2018 20:39:59
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
class Solution {
public:
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        vector<int> char_count(26);
        vector<int> count;
        for(string word : B) {
            count = counter(word);
            for(int i = 0; i < 26; i++) char_count[i] = std::max(count[i], char_count[i]);
        }
        vector<string> result;
        for(string word : A) {
            count = counter(word);
            bool legal = true;
            for(int i = 0; i < 26; i++) {
                if (count[i] < char_count[i]) {
                    legal = false;
                    break;
                }
            }
            if (legal) result.push_back(word);
        }
        return result;
    }
    vector<int> counter(string word) {
        vector<int> count(26);
        for(char c : word) count[c - 'a']++;
        return count;
    }
};