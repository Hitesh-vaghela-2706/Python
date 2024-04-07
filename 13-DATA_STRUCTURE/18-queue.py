# Initializing a queue
queue = []
# Adding elements to the queue
queue.append('x')
queue.append('y')
queue.append('z')
print("Initial queue",queue)
# Removing elements from the queue
print("Elements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print("Queue after removing elements")
print(queue)
print("Elements dequeued from queue")
print(queue.pop(0))
print("Queue after removing elements")
print(queue)
# uncommenting print(queue.pop(0))
# will raise an IndexError if because queue is now empty