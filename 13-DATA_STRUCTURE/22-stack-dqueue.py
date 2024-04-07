# Python program to demonstrate stack implementation using collections.deque
from collections import deque
stack = deque()
# append() function to push element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack:',stack)
# pop() function to pop element from stack in LIFO order
print('Elements popped from stack:')
print(stack.pop())
print(stack.pop())
print('Stack after elements are popped:',stack)
# uncommenting print(stack.pop()) will cause an IndexError as the stack is now empty