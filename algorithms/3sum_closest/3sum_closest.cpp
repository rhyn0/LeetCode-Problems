#include <algorithm>
#include <vector>
#include <unordered_map>
#include <limits>

class Solution {
public:
    int threeSumClosest(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> map; // map values to integers so we can jump around again
        std::vector<int> bestResult;
        int remainder, lowerSum, closestDiff = std::numeric_limits<int>::max();

        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < int(nums.size()); i++)
        {
            map[nums[i]] = i;
        }

        lowerSum = nums[0] + nums[1] + nums[2];
        // if the smallest three numbers exceed the target then it can't go down.
        if (lowerSum >= target) return lowerSum;

        for (int i = 0; i < int(nums.size()); i++)
        {
            for (int j = i + 1; j < int(nums.size()); j++)
            {
                remainder = target - (nums[i] + nums[j]);
                if (map.count(remainder) && map.find(remainder)->second > j){
                    return target;
                }

                for (int z = j + 1; z < int(nums.size()); z++)
                {
                    if (std::abs(remainder - nums[z]) < closestDiff){
                        closestDiff = std::abs(remainder - nums[z]);
                        bestResult = {i, j, z};
                    }
                }
                j = map.find(nums[j])->second;
            }
            i = map.find(nums[i])->second;
        }
        return nums[bestResult[0]] + nums[bestResult[1]] + nums[bestResult[2]];
    }
};

class CommunitySolution{
public:
    int threeSumClosest(std::vector<int>& nums, int target) {
        long int temp, j, z, closestSum = nums[0] + nums[1] + nums[2];

        std::sort(nums.begin(), nums.end());
        // essentially binary search for the complement
        // Make the limit second to last element, since limited by j != z in while
        for (int i = 0; i < int(nums.size()) - 2; i++)
        {
            j = i + 1;
            z = nums.size() - 1;
            while (j < z){
                temp = nums[i] + nums[j] + nums[z];
                if (temp == target) return temp;
                else if (std::abs(target - temp) < std::abs(target - closestSum)) closestSum = temp;
                if (temp < target){
                    j++;
                }
                else{
                    z--;
                }
            }
        }
        return closestSum;
    }
};


#include <iostream>

int main(int argc, char const *argv[])
{
    std::vector<int> exOne = {-1, 2, 1, 4};
    CommunitySolution s;
    std::cout << s.threeSumClosest(exOne, 1) << std::endl;
    return 0;
}
