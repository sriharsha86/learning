''' What is a function in Python?
    A function is a reusable block of code that performs a specific task'''

#example code :
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

''' 2. What is the main difference between return and print in a function?
    print() displays the result to the console
    return sends the result back to the caller for further use'''

def add(a, b):
    return a+b
result = add(5, 3)
print(result) 