#include <vector>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        std::vector<std::vector<int>> ans;
        int remainder, length = nums.size();
        long test;
        std::sort(nums.begin(), nums.end());
        if (length < 4) return {};

        test = nums[0] + nums[1];
        test += nums[2] + nums[3];
        if (test > target) return {};

        test = nums.end()[-1] + nums.end()[-2];
        test += nums.end()[-3] + nums.end()[-4];
        if (test < target) return {};

        for (int i = 0; i < length; i++)
        {
            map[nums[i]] = i;
        }

        for (int i = 0; i < length; i++)
        {
            for (int j = i + 1; j < length; j++)
            {
                for (int k = j + 1; k < length; k++)
                {
                   remainder = target - nums[i] - nums[j] - nums[k];
                   if (map.count(remainder) && map.find(remainder)->second > k)
                   {
                       ans.push_back({nums[i], nums[j], nums[k], remainder});
                   }
                   k = map.find(nums[k])->second;
                }
                j = map.find(nums[j])->second;
            }
            i = map.find(nums[i])->second;
        }
        return ans;
    }
};

#include <algorithm>
#include <vector>
#include <unordered_set>

class OfficialSolution{
public:
    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, int target){
        std::sort(nums.begin(), nums.end());
        return kSum(nums, target, 0, 4);
    }
    std::vector<std::vector<int>> kSum(std::vector<int>& nums, int target, int start, int k){
        std::vector<std::vector<int>> res;
        int average_value;
        if (start == int(nums.size())) return res;

        // use averages to prove whether we can meet our target with k values in a sorted array
        average_value = target / k;

        if (average_value < nums[start] || nums.back() < average_value) return res;

        if (k == 2) return twoSum(nums, target, start);
        for (int i = start; i < int(nums.size()); i++)
        {
            if (i == start || nums[i] != nums[i - 1])
            {
                for (std::vector<int> &vec : kSum(nums, static_cast<long>(target) - nums[i], i + 1, k - 1))
                {
                    res.push_back({nums[i]});
                    res.back().insert(res.back().end(), vec.begin(), vec.end());
                }

            }
        }
        return res;

    }

    std::vector<std::vector<int>> twoSum(std::vector<int>& nums, int target, int start){
        std::vector<std::vector<int>> res;
        std::unordered_set<int> set;

        for (int i = start; i < int(nums.size()); i++)
        {
            if (res.empty() || res.back()[1] != nums[i])
            {
                if (set.count(target - nums[i]))
                {
                    res.push_back({target - nums[i], nums[i]});
                }
            }
            set.insert(nums[i]);
        }
        return res;

    }
};

#include <iostream>

int main(int argc, char const *argv[])
{
    std::vector<int> exTwo = {1,0,-1,0,-2,2};
    OfficialSolution s;
    std::cout << "Solution: ";

    for (auto &&v : s.fourSum(exTwo, 0))
    {
        std::cout << "[";
        for (auto &&x : v)
        {
            std::cout << x << ", ";
        }
        std::cout << "]" << std::endl;
    }
    std::cout << std::endl;

    return 0;
}
