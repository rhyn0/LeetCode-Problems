#include <string>
#include <vector>

class Solution{
    public:
        int romanToInt(std::string s){
            std::vector<std::pair<std::string, int>> mappings = {
                {"M" , 1000},
                {"CM", 900},
                {"D" , 500},
                {"CD", 400},
                {"C" , 100},
                {"XC", 90},
                {"L" , 50},
                {"XL", 40},
                {"X" , 10},
                {"IX", 9},
                {"V" , 5},
                {"IV", 4},
                {"I" , 1}
            };
            int result = 0, j = 0;
            for (int i = 0; i < (int)mappings.size(); i++)
            {
                int cSize = mappings[i].first.size();
                while(j < (int)s.size() && s.substr(j, cSize) == mappings[i].first) result += mappings[i].second, j += cSize;
            }
            return result;
        }
};

class Solution2{
    public:
        int romanToInt(std::string s){
            int result = 0, num;
            for (int i = (int)s.size() - 1; i >= 0; i--)
            {
                switch (s[i])
                {
                case 'I': num = 1; break;
                case 'V': num = 5; break;
                case 'X': num = 10; break;
                case 'L': num = 50; break;
                case 'C': num = 100; break;
                case 'D': num = 500; break;
                case 'M': num = 1000; break;
                }
                if (4 * num < result) result -= num;
                else result += num;
            }
            return result;

        }
};

#include <iostream>
int main(int argc, char const *argv[])
{
    std::string in = "MCMXCIV";
    Solution2 s;
    std::cout << s.romanToInt(in) << std::endl;
    return 0;
}
