# ⬅️Queues in Python
## Overview
### Attributes
Entity Type: Data Structure

### Notes
(1) Linear Data Structure

(2) Follows First In, First Out (FIFO) Principle

### Real-World Applications
(1) **Job Scheduling**
- *Functional Use:* Managing tasks in the order they are received.
- *Applications:* ask scheduling in operating systems, handling print jobs in a printer queue.
- *Real-World Examples:* Operating systems like Linux use queues to manage processes waiting for execution.

(2) **Breadth-First Search (BFS)**
- *Functional Use:* Exploring nodes level by level in a graph or tree.
- *Applications:* Finding shortest paths, exploring neighbors in a maze.
- *Real-World Examples:* Pathfinding algorithms in GPS navigation systems.

(3) **Handling Requests in Networking**
- *Functional Use:* Processing requests in the order they arrive.
- *Applications:* Network request handling in web servers, message queues in distributed systems.
- *Real-World Examples:* Web servers like Apache, Nginx, and message brokers like RabbitMQ use queues to manage incoming requests or messages.

(4) **Buffering in I/O Operations**
- *Functional Use:* Managing data flow to optimize throughput.
- *Applications:* Buffering input/output data in file systems, handling requests to disk or network.
- *Real-World Examples:* Operating systems use queues to manage disk I/O requests and network packet handling.

(5) **Task Management in Concurrent Programming**
- *Functional Use:* Coordinating tasks in concurrent or parallel processing.
- *Applications:* Task queues in multi-threaded or multi-process applications, producer-consumer scenarios.
- *Real-World Examples:* Concurrent programming frameworks like Celery for task queue management in Python applications.

(6) **Event Handling in GUI Applications**
- *Functional Use:* Managing events and user interactions in graphical interfaces.
- *Applications:* Processing user input events (e.g., mouse clicks, keyboard presses) in windowing systems.
- *Real-World Examples:* GUI frameworks like PyQt, Tkinter, and Electron use event queues to manage user interactions.

(7) **Message Queues in Distributed Systems**
- *Functional Use:* Facilitating communication between distributed components.
- *Applications:* Implementing pub/sub models, handling asynchronous communication between microservices.
- *Real-World Examples:* Message queue systems like Kafka, RabbitMQ, and AWS SQS use queues to manage and process messages in distributed architectures.

(8) **Transaction Processing**
- *Functional Use:* Ensuring data integrity and processing transactions in order.
- *Applications:* Processing banking transactions, order processing in e-commerce systems.
- *Real-World Examples:* Banking systems use queues to manage and process financial transactions sequentially.

### Performance
The operations put() and get() on a queue in Python are both O(1), making queues efficient for adding and removing elements in constant time.

## Initialization
Queues can be implemented using the `queue.Queue` class from the `queue` module in Python's standard library. You can initialize a queue like this:
```python
import queue

q = queue.Queue()
```

## Operations
### Notes
The queue data structure operations are known colloquially as the following across most programming languages:

(1) Enqueue - adding an element to the end of the queue. This method is implemented as put() in the `queue.Queue` class in the `queue` module in Python.

(2) Dequeue - removing and returning the element from the front of the queue. This method is implemented as get() in the `queue.Queue` class in the `queue` module in Python.

(3) Empty - checking if the queue is empty. This method is implemented as empty() in the `queue.Queue` class in the `queue` module in Python.

Let's explore some of these implementations in Python.

### Enqueue
```python
q.put(item)
```

### Dequeue
```python
item = q.get()
```

### Empty
```python
if q.empty():
    # queue is empty
```

## Examples

### Sample 1 - Input
```python
import queue

q = queue.Queue()

q.put(1)    # enqueue 1
q.put(2)    # enqueue 2
q.put(3)    # enqueue 3

front = q.get()  # dequeue 1 (first in)
print(front)     # prints 1

front = q.get()  # dequeue 2
print(front)     # prints 2

front = q.get()  # dequeue 3
print(front)     # prints 3

if q.empty():
    print("queue is now empty.")
```

### Sample 1 - Output
```
1
2
3
queue is now empty.
```