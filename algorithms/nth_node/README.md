# Remove Nth Node from End of List

Difficulty: *Medium*

## Description

Given the head of a linked list, remove the nth node from the end of the list and return its head.

![nth node explainer](/leet/img/nth_node.jpg)

Example 1:

```text
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

Example 2:

```text
Input: head = [1], n = 1
Output: []
```

Example 3:

```text
Input: head = [1,2], n = 1
Output: [1]
```

### Constraints

- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

## Initial Thoughts

Annoying part of this is the unknown lenght of the linked list. Going to iterate over it twice, once to find length and the second one to remove said element.

Should be a better way of doing this, but doing this at end of day limits my abilities.

## Post Solve

Forgot to handle the case where $ n \eq len(List) $. Otherwise a simple solution, that gets about 40% on the benchmarks.
