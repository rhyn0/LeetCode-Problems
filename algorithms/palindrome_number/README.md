# Palindrome Number

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Palindrome Number](#palindrome-number)
  - [Description](#description)
    - [Constraints](#constraints)
  - [Initial Solving](#initial-solving)
  - [Post thoughts](#post-thoughts)
  - [Space / Time Analysis](#space-time-analysis)

<!-- /code_chunk_output -->

## Description

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

**Example 1:**

```text
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

**Example 2:**

```text
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```text
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

### Constraints
$$
-2^{31} \leq x \leq 2^{31} - 1
$$

Follow up: Could you solve it without converting the integer to a string?

## Initial Solving

Basically the simplest way is to convert it to a string and then go letter by letter until the middle. I'll figure out this way first then try the extra challenge of doing without the string conversion.

## Post thoughts

String conversion is super easy. Doing the math one is harder. Essentially, instead of trying to treat it like its a string type and do the same matching, track the number in reverse then compare at the end if they are the same.

Such as in 1001: You take the 1001 and build the *01* into another variable but in reverse. So that variable contains *10* which would then be the same as the remainder of the original number.

## Space / Time Analysis

Pretty sure that string conversion method has a $n^2$ time complexity plus the additional **m** space to store the string. Where m is the length of the input int.

Other method has **m** time compleity with constant space complexity, always adding just another int.
