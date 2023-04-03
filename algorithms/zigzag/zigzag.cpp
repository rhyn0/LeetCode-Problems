#include <string>
#include <vector>
#include <iostream>

class Solution{
    public:
        std::string convert(std::string s, int numRows){
            std::string buckets[numRows], receive;
            int incr = -1, bucketNum = 0;
            if (numRows == 1){ return s;}
            for (int i = 0; i < (int)s.size(); i++)
            {
                buckets[bucketNum] += s.at(i);
                if (bucketNum == 0 || bucketNum == numRows - 1) incr *= -1;

                bucketNum += incr;
            }
            for (auto &&i : buckets)
            {
                receive += i;
            }
            return receive;

        }
};

class Solution2{
    public:
        std::string convert(std::string s, int numRows){
            std::string ret;
            std::vector<std::string> rows(std::min(numRows, int(s.length())));
            int curRow = 0;
            bool goingDown = false;
            if (numRows == 1) return s;
            for (char c : s){
                rows[curRow] += c;
                if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
                curRow += goingDown ? 1 : -1;
            }
            for (std::string row : rows) ret += row;
            return ret;
        }
};

class LeetSolution {
public:
    std::string convert(std::string s, int numRows) {

        if (numRows == 1) return s;

        std::string ret;
        int n = s.size();
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < n; j += cycleLen) {
                ret += s[j + i];
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n)
                    ret += s[j + cycleLen - i];
            }
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    std::string input = "AB";
    Solution s;
    std::cout << s.convert(input, 1) << std::endl;
    std::cout << "Expected 'AB'" << std::endl;
    return 0;
}
