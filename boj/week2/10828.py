import sys

class Stack:
    def __init__(self):
        self.length = 0
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
        self.length += 1

    def pop_stack(self):
        if self.size() == 0:
            return -1
        pop_data = self.stack[len(self.stack)- 1]
        self.length -= 1
        del self.stack[self.length]
        return pop_data

    def size(self):
        return self.length
    
    def empty(self):
        return 1 if self.length == 0 else 0

    def top(self):
        return self.stack[-1] if self.size() != 0 else -1

N = int(input())
s = Stack()

for i in range(N):
    a = sys.stdin.readline().split()
    cmd = a[0]

    if cmd == "push":
        s.push(a[1])

    elif cmd == "pop":
        print(s.pop_stack())

    elif cmd == "size":
        print(s.size())

    elif cmd == "empty":
        print(s.empty())

    elif cmd == "top":
        print(s.top())