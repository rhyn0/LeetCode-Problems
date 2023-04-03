# ZigZag Conversion

## Description

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```text
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

`string convert(string s, int numRows);`

**Example 1:**

```text
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```text
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

**Example 3:**

```text
Input: s = "A", numRows = 1
Output: "A"
```

### Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

## Initial thoughts

There is a repeatable pattern for which character goes to which row, so I could figure out how to look at each character in their output order.
But the pattern is kind of annoying, so I'm going to sort the characters in to buckets and then append them at the end.

## Post Solving

Fairly okay approach by statistics, better 60% on both time and space. Going to read the solution and see if any improvements can be made.

## Provided Way of Solving

### Go Character by Character

Their solution uses Vectors, which is a big library which has a lot of load time. My solution is slimmer and faster when run in comparison on LeetCode.

### Go Row by Row

I didn't want to find out the algorithm at the start and here is why:

#### Algorithm

Visit all characters in row 0 first, then row 1, then row 2, and so on...

For all whole numbers $k$:


> Characters in row $0$ are located at indexes $k \; (2 \cdot \text{numRows} - 2)$
> Characters in row $\text{numRows}-1$ are located at indexes $k \; (2 \cdot \text{numRows} - 2) + \text{numRows} - 1$
> Characters in inner row $i$ are located at indices $k \; (2 \cdot \text{numRows}-2)+i$ and $(k+1)(2 \cdot \text{numRows}-2)- i$.

This algorithm is pretty gnarly to figure out by hand after first looking at it. The middle rows are fairly complex with the fact the alternating steps.

Both methods have same time, but the final method technically has constant space complexity. I'll go ahead and past their solution into the file for records.
