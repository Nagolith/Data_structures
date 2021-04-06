from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return self.stack == deque()

    def get_stack(self):
        return self.stack

###########################################
# HERE IS THE SOLUTION TO THE STACK PROBLEM
###########################################
def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    reverse_str = ""

    while not stack.empty():
        reverse_str += stack.pop()

    return reverse_str

###########################################
# END OF SOLUTION
###########################################
stack = Stack()
input_str = input("Please enter a word: ")

print(reverse_string(stack, input_str))
