# Container with Most Water

## Description

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.

![most_water_graph](/leet/img/most_water.png)

**Example 1:**

```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```text
Input: height = [1,1]
Output: 1
```

### Constraints

- n == height.length
- 2 <= n <= $10^5$
- 0 <= height[i] <= $10^4$

## Initial thoughts

This can be considered an optimization problem, might need a greedy algorithm. Just to see it out of my mind I'm going to write a $O(n^2)$ process for it and come back to this spot. Essentially just for each left-hand edge of the container, try each right-hand edge of the container and return max.

## Middle Step

So $O(n^2)$ is too slow, which I expected. The key thing to note is that out of each pair of container edges, I could only _fill_ up to the smaller edge.

Sorting the array doesn't do me a lot of good since order matters. Thought is to sort the array with index pairings -- stopped on this since we aren't looking for greatest heights.

We are trying to maximize the area of the container (area since this is a 2D model, but technically volume but we don't know what the depth is even if it is constant).
So we should find the area of the container based on previous maximum sides found. Bigger sides are helpful as they give us more _volume_ to work with. But also keep track of previous highs as the extra width can outweight the gain in height.

$$
\begin{aligned}
 \text{Given array H of heights of vertical lines;}&\\
 j=\text{position of tallest encountered line, }k=x_j&\\
 y=\text{position of second tallest encountered line, }z=x_y&\\
\end{aligned}\\
\begin{align}
 \text{for } x_i \in H&\text{ DO}\\
 &localArea=max(min(k, x_i) * (i - j), min(z, x_i) * (i - y))\\
 &\text{IF } x_i \gt k\text{ THEN}\\
 &\bullet z=k, y=j\\
 &\bullet k = x_i, j = i\\
 &\text{ELSE IF } x_i \ge z\text{ THEN}\\
 &\bullet z=x_i, y=i\\
 &\text{END IF}\\
 &greatArea=max(localArea, greatArea)\\
 \text{DONE}&\\
 \text{RETURN }& greatArea\\
\end{align}\\
$$

There is probably an edge case that breaks this but it works for the provided examples above as well as:

> 1. [1,2,4,3]
> 1. [1, 8, 9, 1]
> 1. [1,8,6,2,5,4,9,3,7]

Oh, test number 3 above changed to [1,8,6,2,5,4,9,9,3,7] is a failure since I only track out the greatest two. But an easier test case to understand is `[1,2,3,4]` with an expected out of 4 (height 2 for width 2).

## Give up and read

This one seems to be evading my big brain. **HOLY** THATS BIG. Instead of trying to iterate like there is any order, the important thing to understand is that WIDTH is the important value to control. I can't control what the input heights are or how many there are, but I can approach the possible answers with the biggest widths first.

By controlling the width and decreasing it one by one is the best way to $O(n)$ iterate over it. Better than approaching the array as the correct order to iterate over it. Also this solution comes with constant space as a bonus.
