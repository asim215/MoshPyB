from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

popl = queue.popleft()

print(popl, queue)

if not queue:
    print("queue is empty")
