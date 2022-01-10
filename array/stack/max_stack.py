class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self,num):
        self.maxStack.append(max(num,self.max()))
        self.stack.append(num)

    def pop(self):
        self.maxStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def max(self):
        return self.maxStack[-1]
