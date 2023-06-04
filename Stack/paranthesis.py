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

paranthesis = {
    '(':')',
    '[':']',
    '{':'}'
}
stack = Stack()
def check(exp):
    for char in exp:
        if char in paranthesis:
            stack.push(char)
        else:
            if char == paranthesis[stack.top()]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    return False

exp = input("Enter the expression: ")

print(check(exp))



