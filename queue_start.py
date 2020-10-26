# try out the Python queue functions
from collections import deque


# TODO: create a new empty deque object that will function as a queue
stack = [] # declare an empty list
queue = deque()



# TODO: add some items to the queue
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)


queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)




# TODO: print the queue contents
print("The stack is: \n: ", stack)
print("the queue is \n: ", queue)

# TODO: pop an item off the front of the queue
y = queue.popleft()
print("element popped out from the queue: ",y)
print("the queue after: ", queue)


x = stack.pop()
print("element popped: ", x)
print("stack after pop out  and element: ", stack)

