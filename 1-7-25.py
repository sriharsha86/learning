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


'''What is recursion? Give an example
    Recursion is when a function calls itself to solve a smaller instance of the problem'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

'''Wrtie a recursive function to find the nth Fibonacci number'''

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

'''What is the difference between parameters and arguements in a function?'''
#Parameters are variable listed in the function defination
#Arguements are values passed to the function calling it

def greet(name): # name is a parameter here
    print("Hello", name)

greet("Alice") # "Alice" is an arguement

'''Write a function with a default parameter'''
def power(base, exponent=2):
    return base ** exponent

print(power(3))  #output : 9 (since there is a default parameter)
print(power(3, 3)) #output : 27 (since arguemnt is given)


'''Can function retrun multiple values? Demonstrate'''
#yes, using tuple (implicit)

def get_stats(x, y):
    return x + y, x-y

add, sub = get_stats(10, 5)
print(add, sub) # output : 15 5

'''Write a recursive function to find the sum of first n natural numbers'''

def sum_natural(n):
    if n == 1 :
        return 1
    return n + sum_natural(n - 1)

print(sum_natural(5)) #Output : 15

'''What will be the output of this recursive function ?

def mystery(n):
    if n == 0:
        return 0
    return n + mystery(n - 1)
    
print(mystery(4))
'''

# its a recursive function and arguemnt given to it 4
# so the answer would be 4 + 3 + 2 + 1 = 10


""" 5 PROBLEMS REALTED TO RECURSION """

'''Write a recursive function to compute the factorial of a given number n
    Example : factorial(5) -> 120'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))


'''Write a recusrive function to return the nth term in the Fibonacci series
Example : fibonacci(6) -> 8'''

def fibonacci(n) :
    if n <= 1:
        return n    
    return fibonacci(n - 1) + fibonacci(n - 2)
    
for i in range(7):
    print(fibonacci(i), end = " ")


'''Write a recursive function that reverses a string'''

def reverse(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse(s[:-1])

print(reverse("hello"))

'''Wrire a recursive function to find the sum of the digits of a number'''

def sum_digits(n):
    if n == 0 :
        return 0
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(1234))


'''Write a recursive function to find the Greatest Common Divisor of two numbers'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))
