# #️⃣ Hash Maps / Tables in Python
## Overview
### Attributes
Entity Type: Data Structure

### Notes
Ok. So you may have heard of hash maps. You may have heard of hash tables. What's the difference between these two things? It can be a bit tricky. The terms "hash table" and "hash map" are often used interchangeably and can refer to the same fundamental data structure, but in some contexts, there can be subtle distinctions:

#### Hash Table
- **Definition:** A hash table is a data structure that implements an associative array abstract data type, where data elements are stored in an array format, indexed by a hash function that computes an index into an array of buckets or slots.
- **Key Characteristics:**
  - Uses a hash function to compute an index.
  - Supports key-value pairs where keys are hashed to produce indices for fast data retrieval.
  - Typically provides operations for insertion, deletion, and lookup with average constant time complexity (O(1)).

#### Hash Maps
- **Definition:** A hash map is a type of hash table that specifically refers to a data structure that implements a map abstract data type, providing key-value mappings. In many programming languages and contexts, "hash map" is used synonymously with "hash table."
- **Key Characteristics:**
  - Provides a mapping from keys to values.
  - Uses hashing to compute indices for storing and retrieving values based on their keys.
  - Allows efficient insertion, deletion, and lookup operations.

#### Distinctions (If Any)
- **Usage Context:** In some programming languages or academic contexts, "hash map" might emphasize the usage of a hash table specifically for mapping keys to values, focusing on the associative array aspect more than the underlying array and hashing mechanism.
- **Implementation Details:** The term "hash table" might be more general and refer to any implementation of a hash-based data structure, while "hash map" could imply a more specific usage in terms of key-value mappings.

#### Practical Use
- **In Programming Languages:** Languages like Java use the term "HashMap" for their implementation of a hash table that maps keys to values.
- **In Academic Discourse:** Depending on the context, professors or textbooks might use "hash table" to describe the data structure conceptually and "hash map" to emphasize its use as a mapping tool.

#### In Summary
While both terms often refer to the same underlying data structure, "hash table" tends to be more general and can refer to any hash-based data structure, while "hash map" sometimes emphasizes the key-value mapping aspect of a hash table implementation. The exact usage and distinction can vary based on context and language conventions.

#### In Python
Hash maps (often referred to as dictionaries) and hash tables are implemented using the built-in dict data structure. Further below a breakdown of hash maps (dictionaries) and hash tables in Python.

### Real-World Applications
1. **Mapping Unique Keys to Values**
   1. *Functional Use:* Storing and retrieving values based on unique keys.
   2. *Applications:* Storing user information (username to profile data), managing configuration settings (key to value mappings).
   3. *Real-World Examples:* Web applications use dictionaries to map user sessions (session IDs to session data), configuration files (key-value pairs for settings).

2. **Fast Lookup and Retrieval**
   1. *Functional Use:* Efficiently accessing data based on keys without needing to iterate through large datasets.
   2. *Applications:* Database indexing (mapping primary keys to records), caching frequently accessed data (key to cached results).
   3. *Real-World Examples:* Web frameworks like Django use dictionaries extensively for fast database lookups and caching mechanisms.

3. **Counting and Frequency Analysis**
   1. *Functional Use:* Counting occurrences of items or analyzing frequency distribution.
   2. *Applications:* Word count in text processing (word to frequency mapping), tracking item frequency in datasets.
   3. *Real-World Examples:* Natural language processing tasks use dictionaries to analyze word frequencies and perform text analytics.

4. **Grouping and Aggregation**
   1. *Functional Use:* Grouping related data under common keys.
   2. *Applications:* Grouping data by categories (key to list of related items), aggregating statistics (key to cumulative values).
   3. *Real-World Examples:* Data analysis and reporting tools use dictionaries to group data by dimensions (e.g., time series data aggregated by date).

5. **Efficient Parameter Passing and Data Structures**
   1. *Functional Use:* Passing and managing parameters with named keys.
   2. *Applications:* Function arguments and return values (dictionary of parameters), representing complex data structures (nested dictionaries for hierarchical data).
   3. *Real-World Examples:* APIs and web services often use dictionaries to handle request parameters and responses in a structured format.

6. **Error Handling and Lookup Tables**
   1. *Functional Use:* Handling exceptions and managing lookup tables.
   2. *Applications:* Mapping error codes to descriptive messages, maintaining lookup tables for quick reference.
   3. *Real-World Examples:* Software applications use dictionaries to manage error handling (error code to error message mappings) and maintain lookup tables for efficient data retrieval.

7. **Configurable Data Structures and Settings**
   1. *Functional Use:* Storing configurable settings and dynamic data structures.
   2. *Applications:* Application settings (key to configuration values), dynamic data structures (mapping for customizable data formats).
   3. *Real-World Examples:* Software frameworks use dictionaries to manage application configurations and customize data structures based on user-defined preferences.

### Performance
Average Time Complexity: Insertions, deletions, and lookups in Python dictionaries have an average time complexity of O(1), making them highly efficient for operations even with large data sets.

## Hash Maps (Dictionaries) in Python
### Overview
- **Definition:** In Python, a hash map is implemented as a dictionary (dict). It is a collection of key-value pairs where each key is unique and maps to a value.
- **Key Characteristics:** 
  - *Hashing Mechanism:* Python dictionaries use a hash table implementation internally to store and retrieve key-value pairs efficiently.
  - *Fast Lookup:* Allows for average constant-time complexity (O(1)) for insertions, deletions, and lookups.
  - *Mutable:* Dictionaries in Python are mutable, meaning you can change their contents after they are created.
  - *Dynamic Sizing:* Python dictionaries automatically resize themselves as more elements are added.

### Initialization
In Python, dictionaries (`dict`) are a built-in data type and do not require importing any specific class or module to use them. They are part of Python's core data structures and are available by default in any Python script or module. Here are all the ways how you can initalize a dictionary in Python:

1. Literal Syntax
   - Using curly braces {} and separating key-value pairs with colons :. Keys are typically strings or numbers, and values can be any Python object.
```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```

2. Using the `dict()` Constructor
   - Using the built-in `dict()` constructor with key-value pairs provided as arguments or using keyword arguments.
```python
my_dict = dict(key1='value1', key2='value2')
```

3. From Sequence
   - Creating dictionaries from sequences like lists or tuples where each element is a pair of key and value.
```python
pairs = [('key1', 'value1'), ('key2', 'value2')]
my_dict = dict(pairs)
```

4. Using Dictionary Comprehension
   - Creating dictionaries dynamically using comprehensions.
```python
keys = ['key1', 'key2']
values = ['value1', 'value2']
my_dict = {k: v for k, v in zip(keys, values)}
```

- **More Examples of Initialization**
```python
# Using literal syntax
my_dict = {'a': 1, 'b': 2}

# Using dict() constructor
another_dict = dict(x=3, y=4)

# From sequences
pairs = [('c', 5), ('d', 6)]
more_dict = dict(pairs)

# Dictionary comprehension
keys = ['e', 'f']
values = [7, 8]
dict_comp = {k: v for k, v in zip(keys, values)}
```

- **Considerations and Tips**
  - *Immutable Keys:* Keys in a dictionary must be immutable types like strings, numbers, or tuples (containing only immutable elements).
  - *Overwriting Values:* If a key already exists in the dictionary, assigning a new value to that key overwrites the existing value.
  - *Ordering:* Python dictionaries maintain insertion order from Python 3.7 onwards (guaranteed as of Python 3.7+ due to language specification).
  - *Dictionary Methods:* Dictionaries provide methods to manipulate, access, and iterate over their keys, values, and items (keys(), values(), items(), update(), pop(), etc.).

- **Importing Modules for Related Functionality**
  - While dictionaries themselves do not require imports, there are modules and related functions that you might import depending on specific tasks or operations you perform with dictionaries:
    - (1) *Built-In Functions:* Python provides built-in functions like len(), list(), tuple(), etc., which can be used with dictionaries without any import.
    - (2) *Module for Iteration:* If you need to iterate over dictionaries, you might use the items() method directly on the dictionary, but for more advanced iteration techniques or compatibility across Python versions, you might use the six module: 

### Usage
- **Creating A Dictionary:**
```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```

- **Accessing Values:**
```python
value = my_dict['key1']
```

- **Inserting and Updating Values:**
```python
my_dict['new_key'] = 'new_value'  # Inserting a new key-value pair
my_dict['key1'] = 'updated_value'  # Updating an existing value
```

- **Deleting Values:**
```python
del my_dict['key2']
```

- **Iterating Over Keys and Values:**
```python
for key in my_dict:
    print(key, my_dict[key])
```

## Examples

### Sample 1 - Input
```python
# Creating a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Accessing values
print(my_dict['key1'])  # Output: value1

# Adding a new key-value pair
my_dict['key3'] = 'value3'

# Iterating over keys and values
for key, value in my_dict.items():
    print(key, value)
```

### Sample 1 - Output
```
value1
key1 value1
key2 value2
key3 value3
```

### Sample 2 - Input
```python
# Creating a dictionary
my_dict = {'apple': 5, 'banana': 3, 'orange': 7}

# Accessing value
print(my_dict['apple'])  # Output: 5

# Inserting a new key-value pair
my_dict['grape'] = 10

# Updating an existing value
my_dict['banana'] = 6

# Deleting a key-value pair
del my_dict['orange']

# Iterating over keys and values
for key, value in my_dict.items():
    print(key, value)
```

### Sample 2 - Output
```
apple 5
banana 6
grape 10
```

## Hash Tables in Python
### Overview
- **Definition:** Regarding the underlying implementation in Python, a hash table is typically implemented using a dictionary (`dict`). A hash table is a data structure that stores key-value pairs, where each key is unique and maps to a value. This makes dictionaries a practical implementation of hash tables in Python due to their efficient key lookup and insertion operations.
- **Key Characteristics:** 
  - *Internal Mechanism:* Python dictionaries use a hash table internally to store key-value pairs. The hash table uses a hash function to compute an index where each key-value pair is stored.
  - *Hash Function:* Python’s hash function is designed to efficiently distribute keys across the hash table, optimizing lookup performance and facilitating fast access to values associated with each key.
  - *Collision Handling:* Python dictionaries employ techniques like open addressing with linear probing to handle hash collisions. This ensures that if multiple keys hash to the same index, they are stored sequentially in the hash table for efficient retrieval.

Suffice to say - Python has already taken care of the hard part - implementing a hash table that has a hash function which has already addressed collision handling in the way of the Python `dict`. There's no reason to do it on your own - to reinvent the wheel so to say... But this is the hash table section... So we're going to do it anyway. 💀😈

### Construction

A hash table has three parts:
- Hash Table Class
  - This is the logic that implements the class so that it can be utilized.
- Hash Function
  - This is the hashing logic that will hash your data elements into the various buckets of the hash table.
- Hash Table Operations
  - These are the operations that will power the hash table, methods such as insert(), lookup(), delete(), etc.

Let's move to the first part of the process...

### Creating the Hash Table Class
This part isn't very hard at all. You're creating a class like any other in Python. The idea is that you create a class that will be useful to you in all your future Python endeavors. You should intend to import and use this class in future projects. All it needs to do is the job you created it for and continue to make sense to you past the day you made it - hopefully being maintainble and scalable into the future for your needs. Here's but one example of the many ways you could approach this step:

```python
class MyHashTable:
    def __init__(self, size=100):
        self.size = size  # Initial size of the hash table
        self.buckets = [[] for _ in range(size)]  # List of empty lists (buckets)
```

- Explanation:
  - The `MyHashTable` class initializes with a specified size (defaulting to 100).
  - `self.buckets` is a list of lists (`size` number of empty lists), which will store key-value pairs as tuples in each bucket.


### Creating the Hash Function
Now this is the step that has the most flair, the most room for creativity, individuality, complexity, and the most room for error. What makes a hash table is its hash function (and I suppose how it chooses to handle the collision handling... so I guess it's a two-part process). The identity of your hash table lies in your hash function - which determines how efficacious it is, how efficient it is, and how likely it is that your hash table will continue to see use in its future. The legacy of your hash table lives or dies off of your hash function.

Here is ours for the time being, to complete this exercise.

```python
def _hash(self, key):
    return hash(key) % self.size
```

- Explanation:
  - `_hash` method calculates the hash value of the key using Python's built-in `hash()` function and then takes modulo self.size to ensure it fits within the range of bucket indices.
  - Is this a great hash function? Not entirely - but it is a simple hash function and will get the job done for now. We'll dig into what makes a good hash function later.

### Creating the Hash Table Operations
We'll create three methods to accompany our new hash table data structure, the `MyHashTable` class. The methods will be defined in the class itself.

1. insert()
2. lookup()
3. delete()

### Insert

```python
def insert(self, key, value):
    index = self._hash(key)
    for i, (k, v) in enumerate(self.buckets[index]):
        if k == key:
            self.buckets[index][i] = (key, value)  # Update value if key exists
            return
    self.buckets[index].append((key, value))  # Add new key-value pair if key doesn't exist
```

- Explanation
  - `insert` method calculates the index using `_hash(key)`.
  - It checks if the `key` already exists in the bucket; if yes, it updates the value; otherwise, it appends a new tuple `(key, value)` to the bucket.

### Lookup
```python
def get(self, key):
    index = self._hash(key)
    for k, v in self.buckets[index]:
        if k == key:
            return v  # Return value if key is found
    raise KeyError(f'Key {key} not found')  # Raise KeyError if key is not found
```

- Explanation
  - `get` method retrieves the `value` associated with the given `key`.
  - It iterates through the bucket identified by the hash of the `key` and returns the `value` if the `key` is found; otherwise, raises a `KeyError`.

### Delete
```python
def delete(self, key):
    index = self._hash(key)
    for i, (k, v) in enumerate(self.buckets[index]):
        if k == key:
            del self.buckets[index][i]  # Delete key-value pair if key is found
            return
    raise KeyError(f'Key {key} not found')  # Raise KeyError if key is not found
```

- Explanation
  - `delete` method removes the key-value pair associated with the given `key` from the bucket.
  - It iterates through the bucket identified by the hash of the `key` and deletes the tuple if the `key` is found; otherwise, raises a `KeyError`.

And that's it! You've now created a hash table. The last step left is to use it. Let's do that.

### Using the Hash Table
Here's an example using the new custom hash table that we've created together.
```python
class MyHashTable:
    def __init__(self, size=100):
        self.size = size  # Initial size of the hash table
        self.buckets = [[] for _ in range(size)]  # List of empty lists (buckets)

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)  # Update value if key exists
                return
        self.buckets[index].append((key, value))  # Add new key-value pair if key doesn't exist

    def get(self, key):
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v  # Return value if key is found
        raise KeyError(f'Key {key} not found')  # Raise KeyError if key is not found

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]  # Delete key-value pair if key is found
                return
        raise KeyError(f'Key {key} not found')  # Raise KeyError if key is not found

# Create an instance of MyHashTable
ht = MyHashTable()

# Insert key-value pairs
ht.insert('a', 1)
ht.insert('b', 2)
ht.insert('c', 3)

# Retrieve values
print(ht.get('a'))  # Output: 1
print(ht.get('b'))  # Output: 2

# Delete a key-value pair
ht.delete('b')
print(ht.get('b'))  # Raises KeyError: 'Key b not found'

```

With the following as the output:
```
1
2
Traceback (most recent call last):
  File "c:\Users\ezbra\Documents\GitHub\The_Snake_Den\Sandbox.py", line 46, in <module>
    print(ht.get('b'))  # Raises KeyError: 'Key b not found'
          ^^^^^^^^^^^
  File "c:\Users\ezbra\Documents\GitHub\The_Snake_Den\Sandbox.py", line 22, in get
    raise KeyError(f'Key {key} not found')  # Raise KeyError if key is not found
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyError: 'Key b not found'
```

## Supplemental Discussions

### The Nature of a Good Hash Function
Let's revisit the conversation of, "what makes a good hash function?" We'll explore it initially from the context of our custom hash function.

```python
def _hash(self, key):
    return hash(key) % self.size
```

The hash function has some characteristics that make it acceptable for certain use cases but is not ideal for all scenarios. Simply, it falls short by not possessing other characteristics. Your first question might be, 

> "Well.. what are these characteristics by which we judge a hash function?"

What a great question.

This is the full list of characteristics pertaining to hash functions that define their effectiveness and suitability for various applications.

1. **Deterministic:** For the same input, a hash function always produces the same output or hash value.
2. **Uniformity:** The hash function should distribute hash values uniformly across its range, minimizing collisions and ensuring that different inputs have an equal chance of mapping to any hash value.
3. **Efficiency:** The hash function should be computationally efficient to compute the hash value for any input.
4. **Pre-Image Resistance:** Given a hash value, it should be computationally difficult to find an input that hashes to that value. This property is crucial for cryptographic hash functions.
5. **Collision Resistance:** It should be difficult to find two different inputs that produce the same hash value. This property is essential to prevent hash collisions, which can degrade performance or compromise security.
6. **Avalanche Effect:** A small change in the input should produce a significantly different hash value. This property ensures that similar inputs produce very different hash outputs, enhancing security and minimizing collisions.
7. **Non-Reversible:** The hash function should not be easily reversed to determine the original input from its hash value, except through brute force methods.
8. **Consistency:** The hash function's output should not change across different platforms or implementations for the same input.
9. **Simplicity:** While not strictly necessary, simpler hash functions are often preferred for their efficiency and ease of implementation, as long as they meet other essential criteria.
10. **Adaptability:** The hash function should be adaptable to different data types and sizes, handling varying input lengths and formats effectively.
11. **Security:** For cryptographic applications, the hash function should resist known attacks and provide a high level of security against manipulation or forgery.
12. **Hashing Speed:** For non-cryptographic applications, the hash function should be fast to compute to optimize performance in hash tables, caches, and similar data structures.

Yup. So these characteristics collectively define the quality and applicability of a hash function for different use cases, ranging from simple data structures like hash tables to critical applications in cryptography and security. Choosing or designing an appropriate hash function involves considering these properties based on the specific requirements and constraints of the application.

Let's dive into the specifics that make up each criterion.

1. **Determinism**
- Criterion: For the same input (key), the hash function must produce the same output (hash value) every time it is called.
- Example: If `hash(key)` yields a specific hash value `h`, then for any subsequent calls to hash(key), it must consistently yield `h`.
- Importance: Determinism ensures predictability and consistency in hash values, which is essential for correct operation in hash tables and similar data structures.

2. **Uniformity**
- Criterion: Hash values should be uniformly distributed across the range of possible hash values, ideally avoiding clustering or biases towards certain values.
- Example: If a hash function maps a set of keys to hash values, each hash value should be equally likely to be assigned to any key, regardless of the distribution of input keys.
- Importance: Uniformity minimizes collisions and ensures efficient and fair usage of hash table slots or other storage structures.

3. **Efficiency**
- Criterion: The hash function should compute the hash value in a reasonable amount of time relative to the size and complexity of the input.
- Example: The computation of hash(key) should be fast enough to not significantly impact the overall performance of operations using hash values, such as insertion, retrieval, or deletion in hash tables.
- Importance: Efficiency is crucial for scalability and responsiveness in applications handling large volumes of data or frequent hash operations.

4. **Pre-Image Resistance**
- Criterion: Given a hash value (`h`), it should be computationally infeasible to determine the original input (`key`) that produced `h` without exhaustive search.
- Example: If `hash(key) = h`, finding `key` given `h` should be difficult or impractical without knowing the original `key`.
- Importance: Pre-image resistance is essential for cryptographic hash functions to ensure that the original data cannot be reconstructed from its hash value, preserving data integrity and security.

5. **Collision Resistance**
- Criterion: It should be difficult to find two distinct inputs (`key1` and `key2`) that produce the same hash value (`hash(key1) = hash(key2)`).
- Example: Even for a large number of inputs, the likelihood of two inputs mapping to the same hash value should be very low, ideally approaching random distribution.
- Importance: Collision resistance prevents unintended conflicts in hash tables and guarantees the reliability of hash-based data structures by minimizing the occurrence of hash collisions.

6. **Avalanche Effect**
- Criterion: A small change in the input (`key`) should result in a significantly different hash value, affecting a large portion of the hash value bits.
- Example: Changing a single bit in `key` should ideally cause a significant change in the resulting hash value, spreading the influence across the hash value's bit representation.
- Importance: The avalanche effect enhances security and reliability by amplifying differences in input data, minimizing patterns or predictability in hash values.

7. **Non-Reversibility**
- Criterion: It should be computationally impractical or impossible to determine the original input (`key`) from its hash value (`hash(key)`), except through exhaustive search.
- Example: Knowing `hash(key)`, it should be difficult to infer or compute `key` directly from the hash value without knowledge of `key`.
- Importance: Non-reversibility ensures that hashed data cannot be easily reconstructed or manipulated, critical for protecting sensitive information and maintaining data integrity.

8. **Consistency**
- Criterion: The hash function should produce consistent hash values across different platforms, implementations, or executions for the same input.
- Example: Running `hash(key)` on different machines or Python versions should yield identical results for identical `key` inputs.
- Importance: Consistency ensures interoperability and reliability in distributed systems or environments with diverse execution contexts.

9. **Simplicity**
- Criterion: The hash function should be straightforward to understand, implement, and verify its correctness.
- Example: The algorithm or method used in the hash function should be concise, avoiding unnecessary complexity or obscure operations.
- Importance: Simplicity facilitates ease of implementation, debugging, and maintenance, benefiting developers and ensuring reliability in diverse applications.

10. **Adaptability**
- Criterion: The hash function should handle a wide range of input types, sizes, and formats effectively.
- Example: It should accommodate various data structures, data sizes, and input types (e.g., strings, integers, complex objects) without requiring significant modification or adjustment.
- Importance: Adaptability ensures versatility and applicability across different applications and use cases, supporting diverse data processing needs.

11. **Security**
- Criterion: The hash function should resist known attacks and manipulation attempts, particularly in cryptographic applications.
- Example: It should be designed to withstand common cryptographic attacks, such as collision attacks, pre-image attacks, and birthday attacks.
- Importance: Security ensures the confidentiality, integrity, and authenticity of hashed data, crucial for protecting sensitive information and maintaining trust in security-sensitive applications.

12. **Hashing Speed**
- Criterion: The hash function should compute hash values quickly relative to the input size and complexity.
- Example: It should perform efficiently even with large datasets or frequent hash operations, minimizing computational overhead and latency.
- Importance: Hashing speed directly impacts application performance, especially in real-time systems, high-throughput environments, or time-sensitive operations.

So now that we're well informed on the qualities of good hash functions - let us evaluate our custom hash function.

### Evaluating Our Hash Function

```python
def _hash(self, key):
    return hash(key) % self.size
```

1. **Deterministic**
- Evaluation: Yes, hash(key) % self.size is deterministic because for the same key and self.size, it will always produce the same hash value.
- Conclusion: It meets the criterion of determinism.

2. **Uniformity**
- Evaluation: The uniformity of hash(key) % self.size depends heavily on the distribution of Python's built-in `hash()` function and the size of self.size. Python's `hash()` function aims to provide good distribution, but the modulo operation alone may not ensure perfect uniformity across all possible inputs.
- Conclusion: It may not meet the strict criterion of uniformity required for some applications, especially those sensitive to collision probabilities.

3. **Efficiency**
- Evaluation: The function hash(key) % self.size is generally efficient. Computing hash(key) and performing modulo operation are computationally inexpensive operations.
- Conclusion: It meets the efficiency criterion for most practical purposes.

4. **Pre-Image Resistance**
- Evaluation: Given the hash value (hash(key) % self.size), it is not computationally difficult to find an input key that hashes to that value. This function does not aim to provide cryptographic security.
- Conclusion: It does not meet the criterion of pre-image resistance, which is typical for non-cryptographic hash functions.

5. **Collision Resistance**
- Evaluation: The function hash(key) % self.size does not include mechanisms to handle collisions beyond simple modulo arithmetic. Collisions can occur, especially if self.size is not sufficiently large relative to the number of keys.
- Conclusion: It does not meet the criterion of collision resistance required for robust hash functions, especially in applications with high collision sensitivity.

6. **Avalanche Effect**
- Evaluation: A small change in the input key typically results in a significantly different hash value due to the properties of Python's `hash()` function and modulo operation.
- Conclusion: It generally meets the criterion of avalanche effect, contributing to its suitability for basic hashing needs.

7. **Non-Reversible**
- Evaluation: The hash function hash(key) % self.size can be reversed by brute force or by testing all possible inputs, especially given its deterministic nature and lack of cryptographic security measures.
- Conclusion: It does not meet the criterion of non-reversibility required for cryptographic hash functions.

8. **Consistency**
- Evaluation: The output of hash(key) % self.size is consistent across different Python sessions and platforms as long as the inputs and self.size remain unchanged.
- Conclusion: It meets the criterion of consistency for practical applications.

9. **Simplicity**
- Evaluation: The function hash(key) % self.size is simple and easy to understand, requiring minimal computational resources.
- Conclusion: It meets the criterion of simplicity, which can be advantageous for basic hashing needs.

10. **Adaptability**
- Evaluation: The function handles different types of key inputs (as supported by Python's `hash()` function), but its adaptability is limited by Python's hash function behavior and the fixed self.size.
- Conclusion: It meets basic adaptability requirements for general-purpose hashing but lacks flexibility for specialized applications.

11. **Security**
- Evaluation: The function hash(key) % self.size does not provide any security guarantees. It is susceptible to collision attacks, where different keys can produce the same hash value due to the modulo operation and potential weaknesses in Python's built-in `hash()` function.
- Conclusion: It does not meet the criterion of security, particularly for applications requiring resistance against intentional manipulation or attacks.

12. **Hashing Speed**
- Evaluation: The function hash(key) % self.size is generally fast. Python's built-in `hash()` function and modulo operation are computationally efficient, making it suitable for applications where rapid hash computation is necessary.
- Conclusion: It meets the criterion of hashing speed, providing quick computations for common hashing tasks in Python applications.

So in summary, this is the criterion diagnostics for our hashing function:

```
  Deterministic: Yes
  Uniformity: No (depends on Python's hash function and self.size)
  Efficiency: Yes
  Pre-image resistance: No (not designed for cryptographic security)
  Collision resistance: No (simple modulo operation lacks collision handling)
  Avalanche effect: Yes
  Non-reversible: No (can be reversed through brute force)
  Consistency: Yes
  Simplicity: Yes
  Adaptability: Limited
  Security: No (vulnerable to collision attacks)
  Hashing speed: Yes
```

We can see where our hash function is sufficient and where it is not.

What's the verdict then?

> While `hash(key) % self.size` exhibits strengths in determinism, efficiency, simplicity, and hashing speed, it lacks critical characteristics such as uniformity, collision resistance, pre-image resistance, non-reversibility, and security. These deficiencies make it unsuitable for applications requiring robust hash functions, such as cryptographic applications or high-performance hash tables where data integrity and security are paramount. For such applications, specialized hash functions designed to meet these criteria are necessary.

And so - due to the lack of important characteristics, we have reason to believe that this hash function is not a great one. Those hash functions that are great can be useful in almost any scenario where hashing is necessary. Great hash functions have nearly all the missing characteristics that our hash function lacks.

Instead, the hash function 

```python
def _hash(self, key): 
  return hash(key) % self.size
```
has some characteristics that make it acceptable for certain use cases but not ideal for all scenarios.

#### Pros
  - It's simple and easy to implement.
  - It leverages Python's built-in `hash()` function, which can handle a wide range of input types, including strings, integers, and tuples.
  - The modulo operation `% self.size` ensures that the hash value falls within the range `[0, self.size-1]`, making it suitable for indexing into an array or list (buckets).

#### Cons
- Uniformity: The distribution of hash values might not be uniform across all possible inputs. Python’s `hash()` function is not designed to be a perfect hash function for all types of data, and the modulo operation alone may not adequately distribute hash values evenly.
- Collision Handling: It does not include collision resolution mechanisms such as chaining or probing, which are crucial for handling cases where multiple keys hash to the same index (collision).
- Security: Lacks security features such as resistance against hash collisions or cryptographic attacks, making it unsuitable for applications requiring data integrity or confidentiality protection - alongside many other missing characteristics here.

#### Considerations for Use Cases

1. Small to Medium Datasets: For applications where the number of unique keys (self.size) is relatively small and known in advance, this hash function can provide acceptable performance.
2. Non-Cryptographic Use: It's suitable for non-cryptographic applications where the priority is simplicity and performance over cryptographic security.
3. Compatibility: Using Python’s `hash()` function ensures compatibility with Python’s data types, making it convenient for general-purpose hashing needs within Python applications.

#### The Nails in the Coffin

Essentially, chief amongst the characteristics - the lack of the following prevents our custom hash function from being considered a great one.
1. **Collision Risk:** Without collision resolution mechanisms, collisions (multiple keys mapping to the same index) can degrade performance and lead to inefficient data retrieval.
2. **Uniformity:** The modulo operation alone may not sufficiently distribute hash values uniformly, leading to potential clustering of keys in certain buckets, especially with poor distribution from Python’s `hash()` function.
3. **Pre-Image Resistance:** Due to its deterministic nature and reliance on Python's hash() function, it lacks pre-image resistance, making it susceptible to reverse engineering attacks where the original key can be deduced from its hash value.
4. **Adaptability:** Limited adaptability for applications requiring specialized hash functions tailored to specific data types or performance requirements beyond basic indexing tasks.

#### Conclusion

While the hash function `hash(key) % self.size` is straightforward and adequate for certain use cases, especially within the context of smaller datasets and non-cryptographic applications, it lacks robustness in terms of uniformity and collision handling required for broader and more demanding applications. For critical applications requiring strong hash function properties (like cryptographic security or large-scale data processing), more advanced hash functions with better distribution and collision resistance are recommended. Thus, while functional, this hash function does not qualify as a great hash function due to its limitations in handling collisions and ensuring uniform distribution of hash values across a wide range of inputs.

### Hash Functions in the Real World

Here are examples of famous well known hash functions.

MD5 (Message-Digest Algorithm 5)

    Creator: Ronald Rivest
    Industry Use: Historically used in cryptographic protocols and checksums. Deprecated for security-sensitive applications due to vulnerabilities.

SHA-1 (Secure Hash Algorithm 1)

    Creator: National Security Agency (NSA) (US)
    Industry Use: Digital signatures, integrity verification. Deprecated in favor of more secure hash functions like SHA-256.

SHA-256 (Secure Hash Algorithm 256-bit)

    Creator: National Security Agency (NSA) (US)
    Industry Use: Cryptographic applications, blockchain technology (e.g., Bitcoin).

CRC32 (Cyclic Redundancy Check 32-bit)

    Creator: Various contributors
    Industry Use: Error detection in network protocols (Ethernet, ZIP files).

MurmurHash

    Creator: Austin Appleby
    Industry Use: General-purpose hash function, used in distributed systems, hash tables, and data serialization.

CityHash

    Creator: Google
    Industry Use: Optimized for hash tables and hash-based data structures in Google's infrastructure.

xxHash

    Creator: Yann Collet (Cyan)
    Industry Use: High-speed non-cryptographic hash function, used in data integrity checks, checksums, and hash tables.

SipHash

    Creator: Jean-Philippe Aumasson and Daniel J. Bernstein
    Industry Use: Designed for protecting against hash-flooding DoS attacks, used in hash tables and security-sensitive applications.

FNV (Fowler-Noll-Vo) Hash

    Creator: Glenn Fowler, Landon Curt Noll, and Kiem-Phong Vo
    Industry Use: General-purpose hashing, often used in hash tables and checksums due to its simplicity and speed.

DJBX33A (Daniel J. Bernstein's Hash Function)

    Creator: Daniel J. Bernstein
    Industry Use: Simple and fast hash function, used in various applications where speed and simplicity are prioritized.

A myriad of these hash functions occupy different niches in the industry, such as the following:

- **Cryptographic Applications:** SHA-256, SHA-1 (for legacy support), and MD5 (for non-critical applications).

- **Data Integrity and Error Detection:** CRC32 in network protocols, checksums in file systems.

- **Performance Critical Systems:** MurmurHash, xxHash, CityHash, and SipHash in distributed systems, databases, and large-scale data processing.

- **Security:** All kinds of hash functions play a critical role in secure communications, digital signatures, and password storage (using salted hashes).