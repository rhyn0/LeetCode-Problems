#include <vector>
#include <algorithm>

class Solution{
    //inspired by LeetSolution
    public:
        int maxArea(std::vector<int> &height){
            int greatArea = 0;
            int left = 0, right = height.size() - 1;
            while (left < right){
                greatArea = std::max(greatArea, (right - left) * std::min(height[left], height[right]));
                if (height[left] <= height[right]){
                    left++;
                }
                else {
                    right--;
                }
            }
            return greatArea;
        }
};

class SlowSolution{
    public:
        int maxArea(std::vector<int> &height){
            int max = 0, size = height.size();
            for (int i = 0; i < size; i++)
            {
                for (int j = i + 1; j < size; j++)
                {
                    max = std::max((j - i) * std::min(height[i], height[j]), max);
                }

            }
            return max;
        }
};

#include <iostream>
int main(int argc, char const *argv[])
{
    std::vector<int> input = {1,2,3,4};
    Solution s;
    std::cout << s.maxArea(input) << std::endl;
    return 0;
}
