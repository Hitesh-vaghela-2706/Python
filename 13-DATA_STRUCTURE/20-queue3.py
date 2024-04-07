# Python program to demonstrate implementation of queue using queue module
from queue import Queue
# Initializing a queue
q = Queue(maxsize = 3)
# qsize() give the maxsize of the Queue
print(q.qsize())
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
print(q)
# Removing element from queue
print("Elements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
q.put(1)
# q.empty used to check queue is empty or not it returns true or false
print("\nEmpty: ", q.empty())
# q.full used to check queue is full or not it returns true or false
print("Full: ", q.full())
# if queue is empty and we try to remove element This would result to stuck into Infinite Loop
print(q.get())
print(q.get())