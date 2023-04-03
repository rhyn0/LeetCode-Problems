#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> letterCombinations(std::string digits) {
        std::vector<std::string> original = {""}, digit_letters;
        if (digits.size() == 0) return {};

        for (auto &&i : digits)
        {
            digit_letters = keypad_letters(i);
            std::vector<std::string> temp;
            for (auto &&s : original)
            {
                for (auto &&c : digit_letters)
                {
                    temp.push_back(s + c);
                }

            }
            original = temp;

        }
        return original;

    }
private:
    std::vector<std::string> keypad_letters(char s){
        switch (s)
        {
        case '2':
            return std::vector<std::string>{"a", "b", "c"};
            break;
        case '3':
            return std::vector<std::string>{"d", "e", "f"};
            break;
        case '4':
            return std::vector<std::string>{"g", "h", "i"};
            break;
        case '5':
            return std::vector<std::string>{"j", "k", "l"};
            break;
        case '6':
            return std::vector<std::string>{"m", "n", "o"};
            break;
        case '7':
            return std::vector<std::string>{"p", "q", "r", "s"};
            break;
        case '8':
            return std::vector<std::string>{"t", "u", "v"};
            break;
        case '9':
            return std::vector<std::string>{"w", "x", "y", "z"};
            break;
        default:
            return {};
            break;
        }
    }
};

#include <vector>
#include <string>
#include <unordered_map>

class CommunitySolution{
std::unordered_map<char, std::string> L{{'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}};
public:
    std::vector<std::string> letterCombinations(std::string digits) {
        int len = digits.size();
        std::vector<std::string> ans;
        if (len == 0) return ans;
        dfs(0, len, "", ans, digits);
        return ans;
    }
    void dfs(int pos, int &len, std::string str, std::vector<std::string> &ans, std::string &D){
        if (pos == len) ans.push_back(str);
        else{
            std::string letters = L[D[pos]];
            for (int i = 0; i < int(letters.size()); i++)
            {
                dfs(pos + 1, len, str + letters[i], ans, D);
            }

        }
    }
};

#include <iostream>

int main(int argc, char const *argv[])
{
    std::string exOne = "222";
    CommunitySolution s;
    std::cout << "Solution: ";
    for (auto &&i : s.letterCombinations(exOne))
    {
        std::cout << i << " ";
    }

    std::cout << std::endl;

    return 0;
}
