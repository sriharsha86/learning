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

'''Write a function to check if a numebr is prime'''
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(12))