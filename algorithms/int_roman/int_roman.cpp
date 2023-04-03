#include <string>
#include <vector>

class Solution{
    public:
        std::string intToRoman(int num){
            std::vector<std::pair<int, char>> mappings = {
                {1000, 'M'},
                {100, 'C'},
                {10, 'X'},
                {1, 'I'}
            };
            char inter[] = {'D', 'L', 'V'};
            std::string result;
            for (int i = 0; i < (int)mappings.size(); i++)
            {
                if (i == 0){
                    result += romanStep(num, mappings[i], '\0', '\0');
                }
                else {
                    result += romanStep(num, mappings[i], inter[i - 1], mappings[i - 1].second);
                }
                num = num % mappings[i].first;
            }
            return result;
        }
    private:
        std::string romanStep(int num, std::pair<int, char> p, char four, char nine){
            int repeat = num / p.first;
            if (repeat == 0){
                return "";
            }
            else if (repeat == 4){
                return p.second + std::string(1, four);
            }
            else if (repeat == 9){
                return p.second + std::string(1, nine);
            }
            else if (repeat == 5){
                return std::string(1, four);
            }
            else if (repeat < 4){
                return std::string(repeat, p.second);
            }
            else {
                return four + std::string(repeat - 5, p.second);
            }
        }
};

class Solution2{
    public:
        std::string intToRoman(int num){
            std::vector<std::pair<int, std::string>> mappings = {
                {1000, "M"},
                {900, "CM"},
                {500, "D"},
                {400, "CD"},
                {100, "C"},
                {90, "XC"},
                {50, "L"},
                {40, "XL"},
                {10, "X"},
                {9, "IX"},
                {5, "V"},
                {4, "IV"},
                {1, "I"}
            };
            std::string result;
            for (int i = 0; num; i++)
            {
                while(num >= mappings[i].first) result += mappings[i].second, num -= mappings[i].first;
            }
            return result;
        }
};

#include <iostream>
int main(int argc, char const *argv[])
{
    Solution2 s;
    int input = 3;
    std::cout << input << std::endl;
    std::cout << s.intToRoman(3) << std::endl;
    return 0;
}
