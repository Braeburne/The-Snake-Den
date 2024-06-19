# ⌚Priority Queues in Python
## Overview
### Attributes
Entity Type: Data Structure

### Notes
(1) A priority queue in Python is a data structure similar to a regular queue but with the added feature that each element has a priority associated with it. Elements with higher priority are dequeued before elements with lower priority.

(2) Elements in the priority queue are stored and retrieved based on their priority. Lower numerical values indicate higher priority.

(3) In Python, the `queue.PriorityQueue` class provides a straightforward implementation using a heap data structure to manage priorities efficiently.

(4) Follows First In, First Out (FIFO) principle.

### Real-World Applications
(1) **Task Scheduling with Priorities**
- *Functional Use:* Managing tasks where some tasks have higher priority than others.
- *Applications:* Job scheduling in operating systems, task management in real-time systems.    
- *Real-World Examples:* Operating systems use priority queues to schedule tasks based on their urgency and importance.

(2) **Shortest Path Algorithms**
- *Functional Use:* Finding the shortest path in graphs or networks.
- *Applications:* Dijkstra's algorithm for shortest path, Prim's algorithm for minimum spanning tree.
- *Real-World Examples:* Routing algorithms in GPS navigation systems use priority queues to efficiently find the shortest path between locations.

(3) **Event-Driven Simulations**
- *Functional Use:* Simulating events where events have different priorities.
- *Applications:* Simulating traffic flow, modeling system behaviors.
- *Real-World Examples:* Simulation software uses priority queues to manage events and simulate real-world scenarios accurately.

(4) **Optimized Resource Allocation**
- *Functional Use:* Allocating resources based on priorities.
- *Applications:* Resource management in cloud computing, scheduling CPU tasks.
- *Real-World Examples:* Cloud service providers use priority queues to manage resource allocation and scheduling of virtual machines based on customer priorities.

(5) **Emergency Service Dispatch**
- *Functional Use:* Dispatching emergency services based on urgency.
- *Applications:* Ambulance dispatching, fire department responses.
- *Real-World Examples:* Emergency response systems use priority queues to dispatch services quickly to critical situations.

(6) **Job Prioritization in Task Queues**
- *Functional Use:* Managing job queues where jobs have different priorities.
- *Applications:* Task scheduling in distributed systems, processing tasks in batch systems.
- *Real-World Examples:* Task management systems like Celery use priority queues to prioritize and manage jobs efficiently across distributed systems.

(7) **Data Compression Algorithms**
- *Functional Use:* Encoding and decoding data efficiently.
- *Applications:* Huffman coding for data compression.
- *Real-World Examples:* Compression utilities use priority queues to build optimal coding trees for efficient data compression and decompression.

(8) **Load Balancing in Networking**
- *Functional Use:* Distributing network traffic based on priority.
- *Applications:* Load balancing in web servers, managing network packet processing.
- *Real-World Examples:* Load balancers use priority queues to prioritize and manage incoming network requests based on predefined rules.

### Performance
Inserting and removing elements in a priority queue (put() and get() operations) typically has a time complexity of O(log n), where n is the number of elements in the queue. This efficiency makes priority queues suitable for applications requiring efficient prioritization.

## Initialization
Priority Queues can be implemented using the `queue.PriorityQueue` class from the `queue` module in Python's standard library. This class uses the heap queue algorithm (or heapq) to manage priorities efficiently. You can initialize a priority queue like this:
```python
import queue

pq = queue.PriorityQueue()
```

## Operations
### Notes
The priority queue data structure operations are known colloquially as the following across most programming languages:

(1) Insert - inserting an element with a priority. This method is implemented as put(priority, item) in the `queue.PriorityQueue` class in the `queue` module in Python. It takes two parameters, the priority and the object itself.

(2) Remove - remove and return the element with the highest priority. This method is implemented as get() in the `queue.PriorityQueue` class in the `queue` module in Python.

(3) Empty - checking if the priority queue is empty. This method is implemented as empty() in the `queue.PriorityQueue` class in the `queue` module in Python.

Let's explore some of these implementations in Python.

### Insert
```python
pq.put((priority, item))
```

### Remove
```python
item = pq.get()
```

### Empty
```python
if pq.empty():
    # priority queue is empty
```

## Examples

### Sample 1 - Input
```python
import queue

pq = queue.PriorityQueue()

pq.put((3, 'task 1'))   # priority 3
pq.put((1, 'task 2'))   # priority 1
pq.put((2, 'task 3'))   # priority 2

while not pq.empty():
    priority, task = pq.get()
    print(f'Processing task: {task} with priority {priority}')
```

### Sample 1 - Output
```
Processing task: task 2 with priority 1
Processing task: task 3 with priority 2
Processing task: task 1 with priority 3
```