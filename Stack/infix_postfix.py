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


class InfixToPostfixConverter:
    def __init__(self):
        self.operators = ['^', '*', '/', '+', '-']
        self.precedence = {'^': 2, '*': 1, '/': 1, '+': 0, '-': 0}
        self.postfix = []

    def convert(self, expression):
        stack = Stack()

        for char in expression:
            if char.isalnum():
                self.postfix.append(char)
            elif char in self.operators:
                while (not stack.is_empty()) and (stack.top() != '(') and (
                        self.precedence[char] <= self.precedence[stack.top()]):
                    self.postfix.append(stack.pop())
                stack.push(char)
            elif char == '(':
                stack.push(char)
            elif char == ')':
                while (not stack.is_empty()) and (stack.top() != '('):
                    self.postfix.append(stack.pop())
                stack.pop()

        while not stack.is_empty():
            self.postfix.append(stack.pop())

        return ''.join(self.postfix)


exp = input("Enter the expression: ")
converter = InfixToPostfixConverter()
postfix_expression = converter.convert(exp)
print("Postfix expression:", postfix_expression)