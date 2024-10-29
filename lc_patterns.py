# LeetCode Patterns in Python

print("## LeetCode Patterns ##\n")

# 1. Prefix Sum Pattern
print("\n# 1. Prefix Sum Pattern")
def prefix_sum(arr):
    """
    Computes prefix sums for an array.
    """
    prefix_sums = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix_sums[i + 1] = prefix_sums[i] + arr[i]
    return prefix_sums

# 2. Two Pointers Pattern
print("\n# 2. Two Pointers Pattern")
def two_pointers(arr, target):
    """
    Finds pairs with two pointers that meet a target sum.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

# 3. Sliding Window Pattern
print("\n# 3. Sliding Window Pattern")
def max_sum_subarray(arr, k):
    """
    Finds the maximum sum of a subarray of size k.
    """
    max_sum, window_sum = 0, sum(arr[:k])
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# 4. Fast and Slow Pointers Pattern
print("\n# 4. Fast and Slow Pointers Pattern")
def has_cycle(head):
    """
    Detects if a linked list has a cycle.
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 5. In-place Linked List Reversal
print("\n# 5. In-place Linked List Reversal")
def reverse_linked_list(head):
    """
    Reverses a linked list in place.
    """
    prev, current = None, head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# 6. Monotonic Stack
print("\n# 6. Monotonic Stack")
def next_greater_element(nums):
    """
    Finds the next greater element for each item in the array.
    """
    stack, result = [], [-1] * len(nums)
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
    return result

# 7. Top-K Elements Pattern
print("\n# 7. Top-K Elements Pattern")
import heapq
def find_top_k_elements(nums, k):
    """
    Finds the K largest elements in an array.
    """
    return heapq.nlargest(k, nums)

# 8. Overlapping Intervals Pattern
print("\n# 8. Overlapping Intervals Pattern")
def merge_intervals(intervals):
    """
    Merges overlapping intervals.
    """
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# 9. Modified Binary Search Pattern
print("\n# 9. Modified Binary Search Pattern")
def search_rotated_array(nums, target):
    """
    Searches in a rotated sorted array.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# 10. Binary Tree Traversal Pattern
print("\n# 10. Binary Tree Traversal Pattern")
def inorder_traversal(root):
    """
    Performs in-order traversal of a binary tree.
    """
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
    dfs(root)
    return result

# 11. Depth-First Search (DFS) Pattern
print("\n# 11. Depth-First Search (DFS) Pattern")
def dfs(graph, start, visited=None):
    """
    Depth-first search in a graph.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# 12. Breadth-First Search (BFS) Pattern
print("\n# 12. Breadth-First Search (BFS) Pattern")
from collections import deque
def bfs(graph, start):
    """
    Breadth-first search in a graph.
    """
    visited, queue = set(), deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# 13. Matrix Traversal Pattern
print("\n# 13. Matrix Traversal Pattern")
def count_islands(grid):
    """
    Counts the number of islands in a 2D grid using DFS.
    """
    def dfs(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '0'
            list(map(dfs, (i+1, i-1, i, i), (j, j, j+1, j-1)))
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

# 14. Backtracking Pattern
print("\n# 14. Backtracking Pattern")
def generate_subsets(nums):
    """
    Generates all subsets of a given list of numbers.
    """
    result = []
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    backtrack(0, [])
    return result

# 15. Dynamic Programming (DP) Pattern
print("\n# 15. Dynamic Programming (DP) Pattern")
def fibonacci(n, memo={}):
    """
    Calculates the nth Fibonacci number using DP.
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]