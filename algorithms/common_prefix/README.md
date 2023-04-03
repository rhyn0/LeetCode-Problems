# Longest Common Prefix

Difficult: **Easy**

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### Example 1

```text
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

### Example 2

```text
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

### Constraints

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lower-case English letters.

## Initial Thoughts

Sort array of strings by length $O(n \log n)$ then choose the smallest element. For each element try to reduce the smallest element to have a matching prefix. If the smallest element goes to size 0, then there is no common and can return.

## Post thoughts

I came to a bad assumption in which I need to sort the array first. While it would be helpful to sort the array, its not necessary. Almost all solutions for this have some linear complexity and all you can do is limit the space usage. I will copy the Leet Binary Search solution since it is really nice.
