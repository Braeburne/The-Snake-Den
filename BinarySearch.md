# 🔎 Binary Search
## Overview
### Attributes
Entity Type: Algorithm

### Notes
- Binary Search is an algorithm.
- It is a member of a class of algorithms known as "Divide and Conquer" algorithms.
- It can only be done on a sorted data structure, like a sorted array.

### Real-World Applications
1. **Mapping Unique Keys to Values**
   1. *Functional Use:* Storing and retrieving values based on unique keys.
   2. *Applications:* Storing user information (username to profile data), managing configuration settings (key to value mappings).
   3. *Real-World Examples:* Web applications use dictionaries to map user sessions (session IDs to session data), configuration files (key-value pairs for settings).
2. Efficient Data Retrieval

    Functional Use: Quickly locate a specific element in a sorted array or list.
    Applications: Searching in large datasets, indexing databases, querying sorted data structures.
    Real-World Examples: Search engines like Google use binary search to quickly find indexed web pages, database systems like MySQL and PostgreSQL use binary search for efficient query processing.

Symbol Tables in Compilers

    Functional Use: Quickly find and retrieve variable and function definitions.
    Applications: Compilers and interpreters, development tools.
    Real-World Examples: GCC and Clang compilers use binary search within symbol tables to resolve identifiers during the compilation process.

File Systems and Data Storage

    Functional Use: Locate files or blocks within sorted file systems or data storage systems.
    Applications: File indexing, data deduplication, version control systems.
    Real-World Examples: NTFS (New Technology File System) uses binary search in its Master File Table (MFT) to locate files quickly, Git uses binary search to find commit points during certain operations.

Libraries and Frameworks

    Functional Use: Implement efficient search functions within data structures.
    Applications: Standard libraries in programming languages, framework utilities.
    Real-World Examples: The C++ Standard Template Library (STL) implements binary search algorithms for containers, Python’s bisect module provides binary search functions.

Networking and Distributed Systems

    Functional Use: Efficiently route and locate nodes or data in distributed networks.
    Applications: Peer-to-peer networks, distributed hash tables.
    Real-World Examples: The Chord protocol for distributed hash tables uses binary search to efficiently route queries within the network, Content Delivery Networks (CDNs) use binary search to find the best server to deliver content.

Gaming and Graphics

    Functional Use: Collision detection and spatial partitioning.
    Applications: Real-time graphics rendering, game physics.
    Real-World Examples: Game engines like Unity and Unreal Engine use binary search algorithms to efficiently handle collision detection and spatial queries within their physics engines.

Optimization Problems

    Functional Use: Find optimal solutions or parameters within a defined range.
    Applications: Tuning algorithm parameters, solving mathematical optimization problems.
    Real-World Examples: Machine learning frameworks like TensorFlow and PyTorch use binary search for hyperparameter tuning, financial models use binary search to find optimal investment strategies.

Search Algorithms in Software Development

    Functional Use: Implement efficient search operations within applications.
    Applications: Text editors, IDEs, and development tools.
    Real-World Examples: Text editors like Sublime Text and Visual Studio Code use binary search for features like "Go to Line" or searching within large files.

Geospatial Applications

    Functional Use: Search within spatial data for geographic information systems (GIS).
    Applications: Mapping, navigation, location-based services.
    Real-World Examples: GIS software like ArcGIS and QGIS use binary search to quickly locate spatial data points, GPS systems use binary search to find the closest map points or routes.

Financial Services

    Functional Use: Analyze and search within sorted financial data.
    Applications: Stock trading, risk management, financial analysis.
    Real-World Examples: Stock trading platforms use binary search to find specific stock prices within historical data, financial analysts use binary search to quickly locate relevant financial metrics.

### Performance
Time Complexity

Binary search operates by repeatedly dividing the search interval in half. The main steps involve:

    Calculate the Middle Index: This operation is a simple arithmetic operation.
    Compare Middle Element with Target: This involves a single comparison.
    Adjust Search Range: Based on the comparison, the search range is halved (either the left or right half).

Given these steps, the time complexity can be derived as follows:

    Best Case: O(1)O(1)
        The target element is found in the first comparison.
    Average Case: O(log⁡n)O(logn)
        On average, each step halves the search range, leading to a logarithmic number of comparisons.
    Worst Case: O(log⁡n)O(logn)
        The search interval is divided in half each time, leading to log⁡nlogn comparisons in the worst case.

Space Complexity

The space complexity of binary search depends on whether it's implemented iteratively or recursively:

    Iterative Binary Search: O(1)O(1)
        Requires a constant amount of space for variables like the start, end, and middle indices.
    Recursive Binary Search: O(log⁡n)O(logn)
        Each recursive call adds a new frame to the call stack, leading to a space complexity proportional to the depth of the recursion, which is log⁡nlogn.

Performance Analysis

Let's break down the performance using the criteria we discussed previously for evaluating hash functions, but adapted for binary search:

    Determinism: Binary search is deterministic. Given the same sorted array and target, it will always follow the same sequence of steps and return the same result.

    Uniformity: Binary search's performance is consistent across any sorted array of the same size. It does not depend on the distribution of elements within the array.

    Collision Resistance: Not applicable. Binary search is not concerned with collisions as in hashing. Instead, it focuses on the position of elements within a sorted array.

    Efficiency: Binary search is highly efficient for large, sorted datasets. With a time complexity of O(log⁡n)O(logn), it significantly outperforms linear search O(n)O(n) for large inputs.

    Simplicity: Binary search is conceptually simple and easy to implement, both iteratively and recursively.

    Stability: Binary search is stable concerning sorted arrays. It does not alter the order of elements.

    Hash Code Distribution: Not applicable. Binary search operates on indices within a sorted array, not hash codes.

    Security: Not applicable. Binary search is not used for cryptographic purposes.

    Hash Key Sensitivity: Not applicable. Binary search does not use keys or hashes but directly compares array elements.

    Low Likelihood of Collisions: Not applicable. Binary search does not involve collisions.

    Hashing Speed: Binary search is fast, with logarithmic time complexity.

    Hashing Space Efficiency: Binary search is space-efficient, especially in its iterative form, with constant space complexity O(1)O(1).

Practical Implications

    Large Sorted Datasets: Binary search excels in environments where data is large and sorted, such as databases, search engines, and data retrieval systems.
    Read-Heavy Operations: Ideal for applications where read operations are frequent and the data is static or infrequently updated.
    Resource-Constrained Environments: Efficient in terms of both time and space, making it suitable for systems with limited resources.

## Examples

### Sample 1 - Input
```python
import math
import random

def binary_search(array, target, start_index, end_index):
    
    print(f"Starting index is {start_index}...")
    print(f"Ending index is {end_index}...")

    if start_index > end_index:
        return "binary search not valid"
    
    middle = start_index + math.floor((end_index - start_index) / 2)
    print(f"Middle is determined to be index {middle}")

    if array[middle] == target:
        return f"Target found at index {middle}"

    if array[middle] > target:
        print(f"Middle value, {array[middle]}, is greater than the target {target}. Adjusting search field...")
        return binary_search(array, target, start_index, middle - 1)

    if array[middle] < target:
        print(f"Middle value, {array[middle]}, is less than the target {target}. Adjusting search field...")
        return binary_search(array, target, middle + 1, end_index)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Contents of the array:")
    for num in arr:
        print(num)
    random_number = random.randint(1, 10)
    target = random_number
    print(f"Target is number {target}")
    print(f"Array length is {len(arr)}")
    print(binary_search(arr, target, 0, len(arr) - 1))

if __name__ == "__main__":
    main()
```

### Sample 1 - Output
Note: Sample 1 generates a random target value for each run, so the expected output will constantly change. Below is an example of one of many expected outputs. If you were to hardcore target to be the value '9', then this would be the expected output each and every time the program is run.
```
Contents of the array:
1
2
3
4
5
6
7
8
9
10
Target is number 9
Array length is 10
Starting index is 0...
Ending index is 9...
Middle is determined to be index 4
Middle value, 5, is less than the target 9. Adjusting search field...
Starting index is 5...
Ending index is 9...
Middle is determined to be index 7
Middle value, 8, is less than the target 9. Adjusting search field...
Starting index is 8...
Ending index is 9...
Middle is determined to be index 8
Target found at index 8
```

### Sample 2 - Input
```python
import math
import random

def binary_search(array, target, start_index, end_index):
    
    print(f"Starting index is {start_index}...")
    print(f"Ending index is {end_index}...")

    if start_index > end_index:
        return "binary search not valid"
    
    middle = start_index + math.floor((end_index - start_index) / 2)
    print(f"Middle is determined to be index {middle}")

    if array[middle] == target:
        return f"Target found at index {middle}"

    if array[middle] > target:
        print(f"Middle value, {array[middle]}, is greater than the target {target}. Adjusting search field...")
        return binary_search(array, target, start_index, middle - 1)

    if array[middle] < target:
        print(f"Middle value, {array[middle]}, is less than the target {target}. Adjusting search field...")
        return binary_search(array, target, middle + 1, end_index)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Contents of the array:")
    for num in arr:
        print(num)
    random_number = random.randint(1, 10)
    target = random_number
    print(f"Target is number {target}")
    print(f"Array length is {len(arr)}")
    print(binary_search(arr, target, 0, len(arr) - 1))

if __name__ == "__main__":
    main()
```

### Sample 2 - Output
Note: Different formula for the middle value, algorithm still works the exact same. If you were to hard code the target value to '9', you'd get the same output as Sample 1. Here's but another example of potential output from Sample 2.
```
Contents of the array:
1
2
3
4
5
6
7
8
9
10
Target is number 7
Array length is 10
Starting index is 0...
Ending index is 9...
Middle is determined to be index 4
Middle value, 5, is less than the target 7. Adjusting search field...
Starting index is 5...
Ending index is 9...
Middle is determined to be index 7
Middle value, 8, is greater than the target 7. Adjusting search field...
Starting index is 5...
Ending index is 6...
Middle is determined to be index 5
Middle value, 6, is less than the target 7. Adjusting search field...
Starting index is 6...
Ending index is 6...
Middle is determined to be index 6
Target found at index 6
```

### Sample 3 - Input
```python
import timeit

# Measure execution time of binary_search
setup = '''
import random
import math

def binary_search(array, target, start_index, end_index):
    if start_index > end_index:
        return "binary search not valid"
    middle = math.floor((start_index + end_index) / 2)
    if array[middle] == target:
        return f"Target found at index {middle}"
    if array[middle] > target:
        return binary_search(array, target, start_index, middle - 1)
    if array[middle] < target:
        return binary_search(array, target, middle + 1, end_index)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = random.randint(1, 10)
'''

stmt = 'binary_search(arr, target, 0, len(arr) - 1)'
print(timeit.timeit(stmt, setup=setup, number=1000))
```

### Sample 3 - Output
Note: In Sample 3, I wanted to use the `timeit` Python module to measure the execution time of the function. This was to see if the execution times would make sense for binary search, which we know to be an algorithm that operates in O(log n) time. Like the others, this output is dynamically generated - and only represents examples of potential output.
```
0.0007260999991558492
0.00043070001993328333
0.0008303999784402549
0.001068799989297986
0.0009205999958794564
```