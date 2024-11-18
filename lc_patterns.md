
# LeetCode Patterns Guide

# Overview

Solving LeetCode problems efficiently often comes down to recognizing patterns. By learning these 15 essential patterns, you can tackle a wide range of problems more effectively.

## 1. Prefix Sum

**Description**: Used for problems where you need to quickly calculate the sum of elements between two indices in an array.

- **When to Use**: When you have multiple queries to sum up subarrays.
- **Key Concept**: Compute prefix sums so that any subarray sum can be derived with the formula:
  - `sum(i to j) = prefix[j] - prefix[i - 1]`
- **Example Problems**:
  - Range Sum Query
  - Subarray Sum Equals K
- **Resources**:
  - [Prefix Sums - Problems, Code in C++ & Python](https://www.youtube.com/watch?v=PhgtNY_-CiY)

## 2. Two Pointers

**Description**: Uses two pointers moving towards each other or in the same direction.

- **When to Use**: Commonly for array and string problems, especially involving comparisons between elements.
- **Key Concept**: Efficiently reduce the search space by managing the two pointers.
- **Example Problems**:
  - Valid Palindrome
  - Container With Most Water

## 3. Sliding Window

**Description**: Useful for finding subarrays or substrings that meet specific criteria (like maximum sum or unique characters).

- **When to Use**: When you need to optimize calculations on overlapping subarrays.
- **Key Concept**: Slide the window to avoid recalculating values by removing the outgoing and adding the incoming element.
- **Example Problems**:
  - Maximum Sum Subarray of Size K
  - Longest Substring Without Repeating Characters


## 4. Fast and Slow Pointers

**Description**: Involves two pointers moving at different speeds, typically one pointer twice as fast as the other.

- **When to Use**: Particularly useful for linked list cycle detection and finding the middle node.
- **Key Concept**: The fast pointer will either catch up or leave the slow pointer, revealing cycles or midpoints.
- **Example Problems**:
  - Linked List Cycle
  - Find the Middle of a Linked List


## 5. In-Place Linked List Reversal

**Description**: Reverses a linked list or modifies its nodes directly without extra space.

- **When to Use**: When a linked list needs to be reversed or reordered without additional memory.
- **Key Concept**: Use three pointers to reverse the `next` pointers while traversing the list.
- **Example Problems**:
  - Reverse Linked List
  - Reverse Nodes in k-Group

## 6. Monotonic Stack

**Description**: Uses a stack to maintain elements in either increasing or decreasing order.

- **When to Use**: To find the next greater or smaller element in an array.
- **Key Concept**: Push elements onto the stack while maintaining a specific order, then pop when the order is violated.
- **Example Problems**:
  - Next Greater Element
  - Largest Rectangle in Histogram

## 7. Top-K Elements

**Description**: Finding the K largest, smallest, or most frequent elements.

- **When to Use**: When problems involve selecting the top K elements from a dataset.
- **Key Concept**: Use a min-heap (or max-heap) to efficiently manage the top K elements.
- **Example Problems**:
  - Kth Largest Element in an Array
  - Top K Frequent Elements


## 8. Overlapping Intervals

**Description**: Useful for merging, intersecting, or inserting intervals.

- **When to Use**: For problems involving ranges that might overlap.
- **Key Concept**: Sort intervals by start time, then merge intervals if they overlap.
- **Example Problems**:
  - Merge Intervals
  - Insert Interval

## 9. Modified Binary Search

**Description**: Extends binary search to handle cases like rotated arrays or partial sorting.

- **When to Use**: For modified sorted arrays or unknown array lengths.
- **Key Concept**: Use additional checks within binary search to adapt it to unsorted or rotated arrays.
- **Example Problems**:
  - Search in Rotated Sorted Array
  - Find Minimum in Rotated Sorted Array

## 10. Binary Tree Traversal

**Description**: Different tree traversal techniques (pre-order, in-order, post-order, level-order).

- **When to Use**: For traversing binary trees in specific ways based on the problem.
- **Key Concept**: Choose traversal order based on what part of the tree you need to process first.
- **Example Problems**:
  - Binary Tree Inorder Traversal
  - Binary Tree Level Order Traversal

## 11. Depth-First Search (DFS)

**Description**: A traversal technique used to explore all paths or branches in graphs and trees.

- **When to Use**: For problems requiring full exploration of nodes.
- **Key Concept**: Use a stack or recursion to dive into each branch before backtracking.
- **Example Problems**:
  - Number of Connected Components in a Graph
  - Path Sum in Binary Tree

## 12. Breadth-First Search (BFS)

**Description**: A traversal technique that explores nodes level by level.

- **When to Use**: For finding the shortest path or all nodes at a specific level.
- **Key Concept**: Use a queue to process nodes level-by-level.
- **Example Problems**:
  - Shortest Path in Binary Matrix
  - Word Ladder

## 13. Matrix Traversal

**Description**: Used for navigating grids, typically in 2D arrays.

- **When to Use**: For problems on grids, including pathfinding and island counting.
- **Key Concept**: Treat the grid as a graph where each cell is a node connected to adjacent cells.
- **Example Problems**:
  - Number of Islands
  - Flood Fill

## 14. Backtracking

**Description**: Used for problems that involve exploring all potential solutions by making and unmaking choices.

- **When to Use**: For generating permutations, combinations, or solving constraint problems.
- **Key Concept**: Make a choice, proceed recursively, and backtrack if the choice is not viable.
- **Example Problems**:
  - Generate Parentheses
  - N-Queens

## 15. Dynamic Programming (DP)

**Description**: Optimizes problems by breaking them into subproblems and storing solutions to avoid redundant calculations.

- **When to Use**: For optimization and counting problems with overlapping subproblems.
- **Key Concept**: Use a table or memoization to store previously computed solutions.
- **Example Problems**:
  - Fibonacci Sequence
  - Longest Increasing Subsequence

Each pattern provides a unique approach to tackling problems, and mastering these patterns can significantly improve your problem-solving skills on platforms like LeetCode. **Happy coding!**

# Deep Dive

## 1. Prefix Sums

### Background

So the first thing to explore is the concept of a prefix? What is it? What about a suffix? This isn't English, what do these words have to do with computer science?

Well, let's start with the definitions.

1. Prefix: 
the portion of the array that starts at the beginning and ends at (and typically includes) a specific index. In other words:
    - The prefix of index `i` includes all elements from the start of the array up to and including the element at index `i`.
2. Suffix:
the portion of the array that starts at (and typically includes) a specific index and extends to the end of the array. In other words:
    - The suffix of index `i` includes all elements from index `i` to the end of the array.

Let's look at an example.

```
Take the values [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], indexed in the array in positions:
                 0  1  2  3  4  5  6  7  8  9
```

If our target is the index 4, that gives us the value 5.

Again, The prefix here are all the numbers that come before and include the target, the value 5, while the suffix is all
the numbers that come after and include the target (the value 5). So in this case, we have:

```
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                 0  1  2  3  4  5  6  7  8  9
                <----Prefix---->   
                            <-----Suffix----->
```

So, the prefix of 5 (index 4) is the subarray [1, 2, 3, 4, 5]
and
the suffix of 5 (index 4) is the subarray [5, 6, 7, 8, 9, 10]

**What is meant by the "typically includes" clauses?**

Typically in programming, the prefixes and suffixes are inclusive of the target index. It is not typical for prefix and suffix definitions to exlcude the target index in them. 
However, you can of course choose to do so if you would like - hence the use of "typically."

**Why is knowing the prefix and suffix of a given index helpful?**

Well a multitude of reasons, but chief among them, the topic of discussion at this moment, is the ability to use prefixes and suffixes in a programming solution pattern that is known as "Prefix Sums."

The idea behind prefix sums is:
1. For a given index, you calculate the cumulative sum of elements **up to and including a given index.**
2. This pre-computed cumulative sum for all indices can then be stored in a separate array, known as the "prefix sum array."
3. Once you have the prefix sum array, it becomes possible to compute the sum of elements within any subarray efficiently, without recalculating the sum for each query.
4. This is typically implemented as a brand new array to hold the prefix sums of the original array.

Let's walk through an example to make this clearer.

**Example 1:**

The prefix sum at index `4` would be:

- Sum of [1, 2, 3, 4, 5] = 1 + 2 + 3 + 4 + 5 = 15
- Note that this includes the value `5` at index `4`.

So the prefix sum at index `4` is the value, `15`. That is the prefix sum at that index. That is the total sum of the elements up to that point of the array.

If you wanted to contextualize this to a real-world example, let's reimagine it that way.

**Example 2:**

Let's say we have the array `rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. This represents the number of people in each room, going from room `0` to room `9`.

There is 1 person in room `0`.<br>
There is 2 people in room `1`.<br>
There is 3 people in room `2`,<br>
etc, etc.

Then I ask you. "How many people are in the first 5 rooms, from room 0 to room 4?"

This is where the prefix sum is helpful, which simply represents "cumulative sum of elements **up to and including a given index.**"

If you've taken statistics, the prefix sum is conceptually similar to the CDF (Cumulative Distribution Function), but for discrete data. 

Just like the CDF represents cumulative probability up to a point, the prefix sum represents the cumulative total of elements in an array up to a given index.

So what is the answer to the question?

Well, if we were to calculate this heuristically, it would look something like this:

How many people are in the first 5 rooms (room 0 to room 4)?

Step-by-step:<br>
- Room 0: 1 person<br>
- Room 1: 2 people<br>
- Room 2: 3 people<br>
- Room 3: 4 people<br>
- Room 4: 5 people<br>

Total = 1 + 2 + 3 + 4 + 5 = 15

However, we can do the same thing with a prefix_sum(index) function.

- prefix_sum(4) = Sum of [1, 2, 3, 4, 5] = 1 + 2 + 3 + 4 + 5 = 15

Yet again, there are 15 people in those first five rooms.

Great, so maybe now you're picturing the real world use for the "Prefix Sums" solution pattern. Let's look at a more rigorous example now.

**Example 3:**

Given the array `arr = [1, 2, 3, 4, 5]`, we will calculate the prefix sum array.

**Step 1:** Start with an empty prefix sum array, `prefix_sum = []`.

**Step 2:** Calculate the cumulative sum for each index:
   - `prefix_sum[0] = arr[0] = 1`
   - `prefix_sum[1] = prefix_sum[0] + arr[1] = 1 + 2 = 3`
   - `prefix_sum[2] = prefix_sum[1] + arr[2] = 3 + 3 = 6`
   - `prefix_sum[3] = prefix_sum[2] + arr[3] = 6 + 4 = 10`
   - `prefix_sum[4] = prefix_sum[3] + arr[4] = 10 + 5 = 15`

So, the prefix sum array is: 

prefix_sum = [1, 3, 6, 10, 15]


**Step 3:** Use the prefix sum array to compute subarray sums efficiently.

```
Input
arr = [1, 2, 3, 4, 5]
       0  1  2  3  4 (indices)
```

For example, if you want the sum of elements from index 1 to 3 (`[2, 3, 4]`):
   - Without prefix sums, you would calculate: `2 + 3 + 4 = 9`
   - With prefix sums:
      - `{Sum(1, 3)} = {prefix_sum[3]} - {prefix_sum[0]} = 10 - 1 = 9`
   - Notice that we subtracted `prefix_sum[0]` because it represents the sum of elements before index 1.

For subarrays starting at index `0`, the sum is simply `prefix_sum[j]` (e.g., `Sum(0, 2) = prefix_sum[2] = 6`).

Once you've precomputed a prefix sum array, you can calculate the sum of any subarray in constant time by subtracting two prefix sums.

**Why is this helpful?**

Using prefix sums makes it possible to compute the sum of any subarray in constant time \(O(1)\) after building the prefix sum array. Building the prefix sum array itself takes \(O(n)\), so this method is highly efficient for repeated subarray sum queries.

**Expanding Prefix Sum to Include Suffix Sum**

A similar concept applies to suffix sums. You can pre-compute a suffix sum array to get the cumulative sum of elements **from a given index to the end of the array**. This is particularly useful for problems that ask for comparisons between prefixes and suffixes.

For example:

arr = [1, 2, 3, 4, 5]

The suffix sum array would be:

suffix_sum = [15, 14, 12, 9, 5]


Where:
- `suffix_sum[0] = arr[0] + arr[1] + arr[2] + arr[3] + arr[4] = 15`
- `suffix_sum[1] = arr[1] + arr[2] + arr[3] + arr[4] = 14`, and so on.

**When to Use Prefix or Suffix Sums in Programming?**

1. **Range Queries**: Efficiently calculate the sum of elements in a subarray.
2. **Subarray Problems**: Solve problems like finding subarrays with a given sum or finding the maximum subarray sum of fixed size.
3. **Optimization Problems**: Compare prefix and suffix sums to divide an array into sections or to balance computations.
4. **Dynamic Programming Problems**: Prefix sums often play a key role in optimizing solutions for array-based problems.

With this understanding, you can see how the concepts of **prefix and suffix** extend beyond their basic definitions to become powerful tools in problem-solving.

### Implementation

#### **Psuedocode**

Steps to Compute a Prefix Sum Array

1. Initialize an empty prefix sum array of the same size as the input array.
2. For the first element:
   - `prefix_sum[0] = arr[0]`
3. For all subsequent elements:
   - `prefix_sum[i] = prefix_sum[i - 1] + arr[i]`

#### **Implementation in Python**

Here is an example of an implementation to compute the prefix sum array and use it to answer range-sum queries efficiently:

```python
def compute_prefix_sum(arr):
    # Step 1: Create an empty prefix sum array
    prefix_sum = [0] * len(arr)
    
    # Step 2: Compute prefix sums
    prefix_sum[0] = arr[0]  # First element is the same
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    return prefix_sum

def range_sum(prefix_sum, left, right):
    # Sum of elements from index `left` to `right`
    if left == 0:
        return prefix_sum[right]
    else:
        return prefix_sum[right] - prefix_sum[left - 1]

# Example usage
arr = [1, 2, 3, 4, 5]
prefix_sum = compute_prefix_sum(arr)
print("Prefix Sum Array:", prefix_sum)  # Output: [1, 3, 6, 10, 15]

# Range sum for subarray [1, 3] (elements 2, 3, 4)
result = range_sum(prefix_sum, 1, 3)
print("Sum of elements from index 1 to 3:", result)  # Output: 9
```
## 11. Depth-First Search (DFS)

## **Background**

So, the first thing to explore is: **What is Depth-First Search (DFS)? Why is it important?**  
DFS is one of the most fundamental graph traversal algorithms. It is a systematic way of exploring all the nodes and edges in a graph. It is widely used in solving problems related to graphs, trees, and grids in programming.

### **What is Depth-First Search?**

**Definition**:  
DFS is an algorithm for traversing or searching through graph or tree data structures. Starting from a node, it explores as far along a branch as possible before backtracking and exploring other branches.

### **Key Characteristics**
1. **Traversal Order**: DFS dives **deep into a branch** before exploring adjacent nodes.
2. **Backtracking**: If a node has no unvisited neighbors, the algorithm backtracks to the previous node to explore other paths.
3. **Data Structures**:
   - **Recursive Approach**: Uses the program's call stack.
   - **Iterative Approach**: Uses an explicit **stack**.

### **DFS in Trees**

In a **tree**, DFS visits:
1. The root node first.
2. Then recursively explores each child node (in a depth-first manner).

Example Tree:

```
    1
   / \
  2   3
 / \
4   5
```

DFS Traversal:  
- Visit `1` → Visit `2` → Visit `4` → Backtrack to `2` → Visit `5` → Backtrack to `1` → Visit `3`.

Result: `[1, 2, 4, 5, 3]`

### **DFS in Graphs**

In a **graph**, DFS explores as deeply as possible along each branch. For graphs, it is important to track visited nodes to avoid revisiting and getting stuck in cycles.

Example Graph:

```
    1 — 2
    |   |
    3 — 4
```

DFS Traversal:  
- Start from `1`: Visit `1` → Visit `2` → Visit `4` → Backtrack to `2` → Backtrack to `1` → Visit `3`.

Result: `[1, 2, 4, 3]`  
(Note: The traversal may vary based on the starting node and graph structure).

### **DFS on Arrays**

While arrays are typically one-dimensional, DFS can be applied in scenarios where you treat an array like a graph. For instance:
    You can imagine indices as nodes and define rules for which indices are "connected."
    DFS can help explore all reachable indices from a starting point.

**Example Problem: Jump Game**

**Problem:** You are given an array of integers where each element represents the maximum number of steps you can jump forward. Determine if you can reach the last index starting from the first.

```python
def can_reach_end(nums):
    def dfs(index):
        if index >= len(nums) - 1:  # Reached or exceeded the last index
            return True
        if index in visited:  # Avoid revisiting
            return False

        visited.add(index)
        max_jump = nums[index]
        for step in range(1, max_jump + 1):  # Explore all possible jumps
            if dfs(index + step):
                return True

        return False

    visited = set()
    return dfs(0)

# Example usage:
nums = [2, 3, 1, 1, 4]
print(can_reach_end(nums))  # Output: True
```

### **DFS on 2D Grids or Matrices**

DFS is extremely useful for solving problems on 2D grids or matrices, which can be thought of as a graph where:

    Nodes are the cells in the grid.
    Edges represent movement to adjacent cells (e.g., up, down, left, right).

**Example Problem: Island Counting**

**Problem:** Given a grid where 1 represents land and 0 represents water, count the number of islands (connected groups of 1s).

```python
def num_islands(grid):
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return
        grid[row][col] = '0'  # Mark the cell as visited
        # Explore all 4 directions
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':  # Found an unvisited island
                dfs(row, col)
                count += 1
    return count

# Example usage:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(num_islands(grid))  # Output: 3
```

### **DFS on Strings**

Strings can be treated as a collection of nodes, especially when combined with a graph-like representation. DFS is used in problems where you need to explore possible combinations or paths through the string.
Example Problem: Word Break

Problem: Given a string s and a dictionary of words, determine if the string can be segmented into a sequence of dictionary words.

```python
def word_break(s, word_dict):
    def dfs(start):
        if start == len(s):  # Reached the end of the string
            return True
        if start in memo:  # Avoid recomputation
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and dfs(end):
                memo[start] = True
                return True

        memo[start] = False
        return False

    memo = {}
    return dfs(0)

# Example usage:
s = "leetcode"
word_dict = {"leet", "code"}
print(word_break(s, word_dict))  # Output: True
```

---

## **When to Use DFS**

1. **Tree and Graph Traversal**:
   - Traverse nodes in a specific order.
2. **Pathfinding**:
   - Find paths from one node to another.
3. **Connected Components**:
   - Determine connected subgraphs.
4. **Topological Sorting**:
   - Use DFS to order tasks in a dependency graph.
5. **Cycle Detection**:
   - Use DFS to detect cycles in a graph.
6. **Solving Mazes**:
   - Explore all possible paths in a grid-based maze.

---

## **Algorithm**

### **Steps for DFS**

1. Start at a given node (root for trees, any node for graphs).
2. Mark the node as visited.
3. Recursively (or iteratively) visit each unvisited neighbor.
4. Backtrack when no unvisited neighbors remain.

---

## **Implementation of DFS**

### **Recursive Implementation**

```python
def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")  # Process the node
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Example usage:
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

visited = set()
print("DFS Traversal (Recursive): ", end="")
dfs_recursive(graph, 1, visited)

## 12. Breadth-First Search (BFS)