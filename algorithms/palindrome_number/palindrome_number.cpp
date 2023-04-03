#include <iostream>
#include <string>

class Solution{
    public:
        bool isPalindrome(int x){
            std::string s = std::to_string(x);
            int str_size = s.size();
            for (int i = 0; i < str_size/ 2; i++)
            {
                if (s.at(i) != s[str_size - i - 1]){ return false;}
            }
            return true;
        }
};

class Solution2{
    public:
        bool isPalindrome(int x){
            if ((x < 0) || (x % 10 == 0 && x != 0)) { return false;}
            int reverse = 0;
            while (x > reverse){
                reverse = reverse * 10 + x % 10;
                x /= 10;
            }
            return (x == reverse) || (x == reverse / 10);
        }
};

int main(int argc, char const *argv[])
{
    Solution2 s = Solution2();
    if (s.isPalindrome(10001)){
        std::cout << "Is palndrome." << std::endl;
    }
    else
    {
        std::cout << "Isn't palindrome." << std::endl;
    }

    return 0;
}
