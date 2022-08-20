import sys

class Queue:
    def __init__(self):
        self.length = 0
        self.queue = []
    
    def push(self, data):
        self.queue.append(data)
        self.length += 1

    def pop_queue(self):
        if self.size() == 0:
            return -1
        pop_data = self.queue[0]
        self.length -= 1
        del self.queue[0]
        return pop_data

    def size(self):
        return self.length
    
    def empty(self):
        return 1 if self.length == 0 else 0

    def front(self):
        return self.queue[0] if self.size() != 0 else -1

    def back(self):
        return self.queue[-1] if self.size() != 0 else -1

N = int(input())
s = Queue()

for i in range(N):
    a = sys.stdin.readline().split()
    cmd = a[0]

    if cmd == "push":
        s.push(a[1])

    elif cmd == "pop":
        print(s.pop_queue())

    elif cmd == "size":
        print(s.size())

    elif cmd == "empty":
        print(s.empty())

    elif cmd == "front":
        print(s.front())

    elif cmd == "back":
        print(s.back())