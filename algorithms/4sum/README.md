# 4Sum

Difficulty: *Medium*

## Description

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

$$
0 \le a, b, c, d \lt n\\
\text{a, b, c, and d are distinct.}\\
nums[a] + nums[b] + nums[c] + nums[d] == target
$$
You may return the answer in any order.

Example 1:

```text
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

Example 2:

```text
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

### Constraints

$$
\begin{equation}
- 1 \le nums.length \le 200
\end{equation}\\
\begin{equation}
- {10}^9 \le nums[i] \le {10}^9
\end{equation}\\
\begin{equation}
- {10}^9 \le target \le {10}^9
\end{equation}
$$

## Initial Thoughts

Possible to create DFS algorithm that only scans forward, thus limiting amount of numbers to search through for answers at final level. But there are also cheats that we know from 3sum that I think are applicable here. Sorting the array is fine, since they don't want the original indices. And since only want unique combinations can use the HashMap to skip over repeat numbers. So no recursion I think.

## Post First Working

Ok well that was super ugly, had to use 3 for loops and just looks like [3sum](/leet/algorithms/3sum/) but for quadruplets. Let's see how community wants to do this.

So official solution continues along like 3Sum, but also points out that this needs to go on for *k* sum in the future. So it is better to handle the *k* case seperately and pass to it whenever we are not at 2 sum. And in the simpler 2 sum case, there is no need for the Map since we are making a single pass over the remaining array looking for a complement to the given target. Which we can just use a HashSet for to prove existence (we don't want indices).

The official solution uses more memory than mine, but has about a 50% speedup compared to mine. And since it is designed for the *k* case, it is much better.
