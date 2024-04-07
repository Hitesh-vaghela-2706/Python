# Python program to demonstrate queue implementation using collections.dequeue
from collections import deque
# Initializing a queue
q = deque()
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
print("Initial queue",q)
# Removing elements from a queue
print("removed element ",q.popleft())
print("Queue after removing elements",q)
# Uncommenting q.popleft() will raise an IndexError as queue is now empty