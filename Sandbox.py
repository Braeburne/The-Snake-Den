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