#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <sstream>

using namespace std;

class Solution {
private:
    struct Node {
        string val;
        bool is_folder;
        unordered_map<string, Node*> next;

        Node(string v) : val(v), is_folder(false) {}
        
        // 析构函数递归删除所有子节点
        ~Node() {
            for (auto& pair : next) {
                delete pair.second;
            }
        }
    };

public:
    vector<string> removeSubfolders(vector<string>& folder) {
        Node* root = new Node("");
        sort(folder.begin(), folder.end());
        vector<string> result;
        
        for (string& f : folder) {
            if (!isSubfolder(f, root)) { 
                result.push_back(f);
            }
        }
        
        delete root;
        return result;
    }

private:
    bool isSubfolder(string folder, Node* root) {
        Node* curr = root;
        bool result = false;
        
        if (!folder.empty() && folder[0] == '/') {
            folder = folder.substr(1);
        }
        
        if (folder.empty()) {
            if (root->is_folder) {
                result = true;
            }
            root->is_folder = true;
            return result;
        }
        
        // 使用字符串流分割路径
        stringstream ss(folder);
        string s;
        
        while (getline(ss, s, '/')) {
            if (curr->next.find(s) != curr->next.end()) {
                curr = curr->next[s];
                if (curr->is_folder) {
                    result = true; 
                }
            } else {
                curr->next[s] = new Node(s);
                curr = curr->next[s];
            }
        }
        
        curr->is_folder = true;
        return result;
    }
};