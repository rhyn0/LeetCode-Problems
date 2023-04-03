# 3Sum Closest

Difficulty: *Medium*

## Description

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

```text
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

Example 2:

```text
Input: nums = [0,0,0], target = 1
Output: 0
```

### Constraints

- 3 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- ${-10}^4 \leq \text{target} \leq {10}^4$

## Initial Thoughts

Just like in 3sum, iterate over the range of numbers. Easy breaks would be:

  1. if a triplet equals target -> immediate return
  1. after sorting, if sum of bottom 3 values is greater than target -> return that sum

Let's try it similar to 3sum, lock in two integers per iteration and use hash map if there is the remaining value.

--------------

Think I messed the problem up in my head. The quick cases are still correct and I can skip over the same number after a failed iteration with it locked in.
Regarding the second point:

```math
a = [2, 2, 2, 3, 4], target = 6
```

Using three 2's is the only close answer for 6 here. But say the target was 9, I can test the locked pair of (2, 2) index -> (0, 1) and get to 8 - a difference of 1. But then my second pointer could skip to the 3 at index 3 instead of trying to loop again with (2, 2) index -> (0, 2).
But in the case that I can't find a perfect triplet that will equal the target - how do I efficiently scan the remaining numbers to find the closest triplet?
Reusing Example 2:

```text
a = [0, 0, 0], target = 1
```

Obviously there can only be the one triplet of (0, 0, 0) which sums to 0. But how did I make that triplet in the case of the two pointer HashMap stye?
$$
i = 0, j = i + 1\
remainder = target - a_i - a_j == 1
\newline
\text{for} j \lt z \lt \lvert a \rvert; \text{ DO}\\
\text{IF } a_z == remainder \text{ THEN}\\
return True\\
\text{ELSE IF } \lvert (a_z - remainder) \rvert \lt closest \text{ THEN}\\
closest = \lvert (a_z - remainder) \rvert;
closestArr = [i, j, z]
$$

## Post Working Thoughts

Impressive to design it and make it work. But sadly it benchmarks at 5%, which means that it is sadly horrible in comparison to what it should be.
I can't decide whether the unordered_map is worth it, since we are looking for closest values maybe it should just be a for loop that goes forward until its greater than remainder.

## Reading Community Solutions

Community seems to conclude that 2 pointer approach is correct and we lock $i$ in each iteration and then find the best Sum per iteration.
I'm hitting overflow errors when writing it, probably because I'm using the numerical limit of int. Going to try using the first sum.

Removing the long int and using an actual sum from the array reduces time by a lot since the limits package seems to test until overflow or something slow.
