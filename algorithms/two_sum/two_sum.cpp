#include <vector>
#include <iostream>
#include <map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++){
            for (int j = i + 1; j < nums.size(); j++)
            {
                /* code */
                if (nums.at(i) + nums.at(j) == target){
                    return std::vector<int> {i, j};
                }
            }
        }
        return std::vector<int>();
    }
};

class Solution2 {
    public:
        std::vector<int> twoSum(std::vector<int>& nums, int target) {
            std::map<int, int> m;
            for (int i = 0; i < nums.size(); i++)
            {
                if (m.find(nums.at(i)) != m.end()){
                    return std::vector<int> {i, m[nums.at(i)]};
                }
                m[target - nums.at(i)] = i;
            }
            return std::vector<int>();

        }
};

int main(int argc, char const *argv[])
{/* code */
    std::vector<int> in_vec{2, 7, 11, 15};
    Solution2 s = Solution2();
    for (auto &&x : s.twoSum(in_vec, 9))
    {
        std::cout << x << " ";
    }
    std::cout << std::endl;

    return 0;
}
