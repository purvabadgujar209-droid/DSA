class stack:
    def __init__(self):
        self.stack = []

    # 1. Push
    def push(self, n):
        self.stack.append(n)

    # 2. Pop
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Popped element:", self.stack.pop())

    # 3. Display
    def display(self):
        print("Stack contains")
        for i in reversed(self.stack):
            print(i)

    print(n, "inserted")

# 2. Pop
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Popped element:", stack.pop())

# 3. Display
def display():
    print("Stack contains")
    for i in reversed(stack):
        print(i)

# 4. Reverse Stack
def reverse_stack():
    stack.reverse()
    print("Reversed Stack:")
    display()

# 5. Reverse String
def reverse_string(s):
    return s[::-1]


# Main Program
push(10)
push(20)
push(30)
push(40)
push(50)

print()
display()

print()
pop()

print()
display()

print()
print("Reversed string:", reverse_string("PYTHON"))

print()
reverse_stack()