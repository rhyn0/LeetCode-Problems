#include <string>
#include <vector>
#include <algorithm>

class Solution{
    public:
        std::string longestCommonPrefix(std::vector<std::string>& s){
            std::string prefix;
            std::vector<std::string> v; // make deep copy since we use reference copy
            for (int i = 0; i < int(s.size()); i++)
            {
                v.push_back(s[i]);
            }

            prefix = v[0];
            for (int i = 1; i < int(v.size()) && prefix.size(); i++)
            {
                while (prefix != v[i].substr(0, prefix.size()))
                {
                    prefix = prefix.substr(0, prefix.size() - 1);
                }
            }
            return prefix;
        }

};

class LeetSolution{
    public:
        std::string longestCommonPrefix(std::vector<std::string>& s){
            int minLen = INT32_MAX, middle, low = 0;
            for (auto &&i : s)
            {
                   minLen = std::min(minLen, int(i.size()));
            }
            while (low <= minLen){
                middle = (low + minLen) / 2;
                if (isCommonPrefix(s, middle)){
                    // become greedy since up to middle is common
                    low = middle + 1;
                }
                else {
                    minLen = middle - 1;
                }
            }
            return s[0].substr(0, (low + minLen) / 2);
        }

    private:
        bool isCommonPrefix(std::vector<std::string> s, int len){
            //is a prefix of given length *len* common across all strings
            std::string prefix = s[0].substr(0, len);
            for (int i = 0; i < int(s.size()); i++)
            {
                if (s[i].find(prefix) != 0) return false;
            }
            return true;
        }
};

#include <iostream>
int main(int argc, char const *argv[])
{
    std::vector<std::string> ins = {"flower","flow","flight"};
    Solution s;
    std::cout << s.longestCommonPrefix(ins) << std::endl;
    return 0;
}
