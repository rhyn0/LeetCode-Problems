#include <iostream>
#include <map>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::map<char, int> m;
        int start = 0, res = 0;
        for (int end = 0; end < s.length(); end++)
        {
            if (m.find(s.at(end)) != m.end()){
                start = std::max(start, m.at(s.at(end)));
            }

            res = std::max(res, end - start + 1);
            m[s.at(end)] = end + 1;
        }
        return res;
    }
};

int main(int argc, char const *argv[])
{
    std::string in = "abcabcbb";
    Solution s = Solution();
    std::cout << s.lengthOfLongestSubstring(in) << std::endl;
    return 0;
}
