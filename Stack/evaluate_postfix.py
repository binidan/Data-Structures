class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
stack = Stack()
input = input("Enter proper postfix expression: ")

for i in input:
    if i.isnumeric():
        stack.push(int(i))
    elif i == '+':
        temp = stack.pop()
        result = stack.pop()+temp
        stack.push(result)
    elif i == '-':
        temp = stack.pop()
        result = stack.pop()-temp
        stack.push(result)
    elif i == '*':
        temp = stack.pop()
        result = stack.pop()*temp
        stack.push(result)
    elif i == '/':
        temp = stack.pop()
        result = stack.pop()/temp
        stack.push(result)
print(stack.stack[0])