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
reverse = ""
input = input("Enter your string: ")

for char in input:
    stack.push(char)

while not stack.is_empty():
    reverse += stack.pop()

print(reverse)