## stacks 
"""
5.1.1. Using Lists as Stacks
The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved 
(“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack,
use pop() without an explicit index. For example:
"""
#LIFO
stack = [3,4,5]
stack.append(6)
stack.append(7)

print(stack)
stack.pop() #pop 7
print(stack)
stack.pop() #pop 6
print(stack)


## Queue - FIFO
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Ravi")
print(queue)

queue.popleft() #ERIC gone 

print(queue)

queue.popleft()
print(queue) #John gone