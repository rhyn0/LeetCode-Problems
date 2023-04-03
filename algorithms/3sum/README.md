# 3Sum

Difficulty: *Medium*

## Description

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

```text
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

Example 2:

```text
Input: nums = []
Output: []
```

Example 3:

```text
Input: nums = [0]
Output: []
```

### Constraints:

- 0 <= nums.length <= 3000
- -105 <= nums[i] <= 105

## Initial thoughts

If there are less than 3 elements, return empty. Otherwise create all possible combinations, and then sum them to keep only the ones that become zero.

Just for fun i'll make the triple for loop one first. WAnt to see performance.
