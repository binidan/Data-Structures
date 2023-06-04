class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def isEmpty(self):
        return not self.stack
    
    def isFull(self):
        if len(self.stack) == self.size:
            return True
        return False
    
    def push(self, value):
        if not self.isFull():
            self.stack.append(value)
        else:
            print("Stack Overflow!")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack Underflow!")

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty")

stack = Stack(5)

stack.push(3)
stack.push(2)
stack.push(9)
stack.push(1)
stack.push(7)
print(stack.top())