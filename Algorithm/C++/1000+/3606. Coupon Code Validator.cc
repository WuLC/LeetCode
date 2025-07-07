#include <vector>
#include <string>
#include <unordered_map>
#include <set>

class Solution {
    public:
        std::vector<std::string> validateCoupons(std::vector<std::string>& codes, std::vector<std::string>& businessLines, std::vector<bool>& isActive) {
            std::set<std::string> b_lines{"electronics", "grocery", "pharmacy", "restaurant"};
            std::unordered_map<std::string, std::vector<std::string>> record;
            for (int i = 0; i < codes.size(); i++) {
                if(isValidCode(codes[i]) && b_lines.find(businessLines[i]) != b_lines.end() && isActive[i]) {
                    record[businessLines[i]].push_back(codes[i]);
                }
            }

            std::vector<std::string> result;
            for (auto bl: b_lines) {
                std::sort(record[bl].begin(), record[bl].end());
                result.insert(result.end(), record[bl].begin(), record[bl].end());
            }
            return result;
        }
    

    private:
        bool isValidCode(std::string& code) {
            if (code.size() == 0) return false;
            for (char c: code) {
                if (!isalnum(c) && c != '_') return false;
            }
            return true;
        }
    };