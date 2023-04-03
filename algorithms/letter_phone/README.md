# Letter Combinations of a Phone Number

Difficulty: *Medium*

## Description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![keypad](../../img/telephone_keypad.png)

Example 1:

```text
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

Example 2:

```text
Input: digits = ""
Output: []
```

Example 3:

```text
Input: digits = "2"
Output: ["a","b","c"]
```

### Constraints

- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9']

## Initial Thoughts

For each number there is a list of possibilites and I have to make the Cartesian product of all the possibilities.

Something like:
    1. For each digit in input
        1. Get list of possible characters
        1. For each character in the input list of strings
            1. Add character on to element in oroiginal list
            1. Add new string to new list
        1. Replace old list with new list

## Post Solve

Not bad on solution. It is super slow due to the triple for loop, so lets see how the solutions gives us some good tips.
Community solution suggests a DFS approach. Which makes sense compared to the BFS search I wrote, since it allows us to use recursion to keep the loops simpler.
Also using an unordered map to a string of values is simpler than return a vector of strings.

It is faster I think to use this way, easier to iterate over and less memory usage - only since input digit string can be a max of 4 characters. But its a very concise solution and easier to understand what is going on.
