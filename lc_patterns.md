
# LeetCode Patterns Guide

## Overview

Solving LeetCode problems efficiently often comes down to recognizing patterns. By learning these 15 essential patterns, you can tackle a wide range of problems more effectively.

---

## 1. Prefix Sum

**Description**: Used for problems where you need to quickly calculate the sum of elements between two indices in an array.

- **When to Use**: When you have multiple queries to sum up subarrays.
- **Key Concept**: Compute prefix sums so that any subarray sum can be derived with the formula:
  - `sum(i to j) = prefix[j] - prefix[i - 1]`
- **Example Problems**:
  - Range Sum Query
  - Subarray Sum Equals K

---

## 2. Two Pointers

**Description**: Uses two pointers moving towards each other or in the same direction.

- **When to Use**: Commonly for array and string problems, especially involving comparisons between elements.
- **Key Concept**: Efficiently reduce the search space by managing the two pointers.
- **Example Problems**:
  - Valid Palindrome
  - Container With Most Water

---

## 3. Sliding Window

**Description**: Useful for finding subarrays or substrings that meet specific criteria (like maximum sum or unique characters).

- **When to Use**: When you need to optimize calculations on overlapping subarrays.
- **Key Concept**: Slide the window to avoid recalculating values by removing the outgoing and adding the incoming element.
- **Example Problems**:
  - Maximum Sum Subarray of Size K
  - Longest Substring Without Repeating Characters

---

## 4. Fast and Slow Pointers

**Description**: Involves two pointers moving at different speeds, typically one pointer twice as fast as the other.

- **When to Use**: Particularly useful for linked list cycle detection and finding the middle node.
- **Key Concept**: The fast pointer will either catch up or leave the slow pointer, revealing cycles or midpoints.
- **Example Problems**:
  - Linked List Cycle
  - Find the Middle of a Linked List

---

## 5. In-Place Linked List Reversal

**Description**: Reverses a linked list or modifies its nodes directly without extra space.

- **When to Use**: When a linked list needs to be reversed or reordered without additional memory.
- **Key Concept**: Use three pointers to reverse the `next` pointers while traversing the list.
- **Example Problems**:
  - Reverse Linked List
  - Reverse Nodes in k-Group

---

## 6. Monotonic Stack

**Description**: Uses a stack to maintain elements in either increasing or decreasing order.

- **When to Use**: To find the next greater or smaller element in an array.
- **Key Concept**: Push elements onto the stack while maintaining a specific order, then pop when the order is violated.
- **Example Problems**:
  - Next Greater Element
  - Largest Rectangle in Histogram

---

## 7. Top-K Elements

**Description**: Finding the K largest, smallest, or most frequent elements.

- **When to Use**: When problems involve selecting the top K elements from a dataset.
- **Key Concept**: Use a min-heap (or max-heap) to efficiently manage the top K elements.
- **Example Problems**:
  - Kth Largest Element in an Array
  - Top K Frequent Elements

---

## 8. Overlapping Intervals

**Description**: Useful for merging, intersecting, or inserting intervals.

- **When to Use**: For problems involving ranges that might overlap.
- **Key Concept**: Sort intervals by start time, then merge intervals if they overlap.
- **Example Problems**:
  - Merge Intervals
  - Insert Interval

---

## 9. Modified Binary Search

**Description**: Extends binary search to handle cases like rotated arrays or partial sorting.

- **When to Use**: For modified sorted arrays or unknown array lengths.
- **Key Concept**: Use additional checks within binary search to adapt it to unsorted or rotated arrays.
- **Example Problems**:
  - Search in Rotated Sorted Array
  - Find Minimum in Rotated Sorted Array

---

## 10. Binary Tree Traversal

**Description**: Different tree traversal techniques (pre-order, in-order, post-order, level-order).

- **When to Use**: For traversing binary trees in specific ways based on the problem.
- **Key Concept**: Choose traversal order based on what part of the tree you need to process first.
- **Example Problems**:
  - Binary Tree Inorder Traversal
  - Binary Tree Level Order Traversal

---

## 11. Depth-First Search (DFS)

**Description**: A traversal technique used to explore all paths or branches in graphs and trees.

- **When to Use**: For problems requiring full exploration of nodes.
- **Key Concept**: Use a stack or recursion to dive into each branch before backtracking.
- **Example Problems**:
  - Number of Connected Components in a Graph
  - Path Sum in Binary Tree

---

## 12. Breadth-First Search (BFS)

**Description**: A traversal technique that explores nodes level by level.

- **When to Use**: For finding the shortest path or all nodes at a specific level.
- **Key Concept**: Use a queue to process nodes level-by-level.
- **Example Problems**:
  - Shortest Path in Binary Matrix
  - Word Ladder

---

## 13. Matrix Traversal

**Description**: Used for navigating grids, typically in 2D arrays.

- **When to Use**: For problems on grids, including pathfinding and island counting.
- **Key Concept**: Treat the grid as a graph where each cell is a node connected to adjacent cells.
- **Example Problems**:
  - Number of Islands
  - Flood Fill

---

## 14. Backtracking

**Description**: Used for problems that involve exploring all potential solutions by making and unmaking choices.

- **When to Use**: For generating permutations, combinations, or solving constraint problems.
- **Key Concept**: Make a choice, proceed recursively, and backtrack if the choice is not viable.
- **Example Problems**:
  - Generate Parentheses
  - N-Queens

---

## 15. Dynamic Programming (DP)

**Description**: Optimizes problems by breaking them into subproblems and storing solutions to avoid redundant calculations.

- **When to Use**: For optimization and counting problems with overlapping subproblems.
- **Key Concept**: Use a table or memoization to store previously computed solutions.
- **Example Problems**:
  - Fibonacci Sequence
  - Longest Increasing Subsequence

---

Each pattern provides a unique approach to tackling problems, and mastering these patterns can significantly improve your problem-solving skills on platforms like LeetCode.

**Happy coding!**
