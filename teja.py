 from collections import deque
class Queue:
    def ＿init＿(self):
     self.queue = deque()
    def insert(self, item):
     self.queue.append(item)
    def delete(self):
     if len(self.queue) > 0:
     else:
         return self.queue.popleft()
    def ＿str＿(self):
        return str(self.queue)
my_queue = Queue()
