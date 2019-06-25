# baek10828(스택)

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, v):
        self.stack.append(v)

    def pop(self):
        if len(self.stack):
            print(self.stack.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.stack))

    def empty(self):
        if len(self.stack):
            print(0)
        else:
            print(1)
    
    def top(self):
        if len(self.stack):
            print(self.stack[-1])
        else:
            print(-1)

s = Stack()

N = int(input())
for _ in range(N):
    line = input().split()
    cmd = line[0]
    if len(line)>1:
        val = line[1]
    if cmd=='push':
        s.push(int(val))
    elif cmd=='pop':
        s.pop()
    elif cmd=='size':
        s.size()
    elif cmd=='empty':
        s.empty()
    else:
        s.top()



