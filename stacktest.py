from collections import deque
my_queue = deque()
my_queue.append(120)
my_queue.append(220)
my_queue.append(180)
print(my_queue.popleft())

#from collections import deque
class queue:
    def __init__(self):
        self.queue=deque()
    def insert(self,item):
        self.queue.append(item)
        def








