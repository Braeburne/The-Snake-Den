import queue

pq = queue.PriorityQueue()

pq.put((3, 'task 1'))   # priority 3
pq.put((1, 'task 2'))   # priority 1
pq.put((2, 'task 3'))   # priority 2

while not pq.empty():
    priority, task = pq.get()
    print(f'Processing task: {task} with priority {priority}')