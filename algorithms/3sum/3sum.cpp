#include <vector>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::unordered_map<int, int> map;
        std::vector<std::vector<int>> ret;
        int required;

        std::sort(nums.begin(), nums.end()); // sort to filter out combinations like +,+,+

        if (nums.size() < 3) return {};
        if (nums[0] > 0) return {}; // if the smallest number is +, then 0 can never be reached

        for (int i = 0; i < int(nums.size()); i++)
        {
            map[nums[i]] = i; // initialize with indices, so duplicates only get the last idnex of their occurrence
        }

        for (int i = 0; i < int(nums.size()); i++) // fix a number of the triplet for each iteration
        {
            if (nums[i] > 0) break; // if the fixed is positive, we only scan forward in a sorted array

            for (int j = i + 1; j < int(nums.size()); j++)
            {
                required = -1 * (nums[i] + nums[j]);

                // as long as the index of required is greater than where we are, it can be a valid triplet
                if (map.count(required) && map.find(required)->second > j)
                {
                    ret.push_back({nums[i], nums[j], required});
                }
                // since we don't accept duplicate answers (duplicate values, not unique useages)
                j = map.find(nums[j])->second;
            }
            i = map.find(nums[i])->second;
        }
        return ret;
    }
};


#include <iostream>

int main(int argc, char const *argv[])
{
    std::vector<int> exOne = {-1,0,1,2,-1,-4};
    // std::vector<int> exTwo = {0};
    // std::vector<int> exThree = {};

    Solution s;

    for (auto &&l : s.threeSum(exOne))
    {
        for (auto &&x : l)
        {
            std::cout << x << ',';
        }
        std::cout << std::endl;

    }

    // std::cout << s.threeSum(exOne).size() << std::endl;
    // std::cout << s.threeSum(exTwo).size() << std::endl;
    // std::cout << s.threeSum(exThree).size() << std::endl;


    return 0;
}
