# Integer to Roman

## Description

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

> Symbol       Value
> I             1
> V             5
> X             10
> L             50
> C             100
> D             500
> M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

### Example 1

```text
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
```

### Example 2

```text
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

### Example 3

```text
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

### Constraints

- 1 <= num <= 3999

## Initial thoughts

Essentially start at biggest values and divide until less than said value. Based on number of times divided can apply the special rules for 4 and 9.
Divide by powers of 10.

## Post completion

Simple problem, I don't think I handle the string creation well but each case is essentially. Maybe i could break the smaller step into using divide by 5 also.

## Leet Code Solution

The official solution is paywalled. Based on [discussion](https://leetcode.com/problems/integer-to-roman/discuss/1102775/JS-Python-Java-C++-or-Simple-Solution-w-Explanation) I'm slowing myself down by limiting my divisions to powers of 10. Just do all possibilities including the 4 and 9 special case. LeetCode isn't perfect on runtimes but it is funny that this solution is technically more memory intensive and slower than mine.
