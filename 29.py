def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
fibonacci(10)

def fibonacci(n):  # Function to print Fibonacci numbers up to n
    a, b = 0, 1  # Initializing first two Fibonacci numbers
    for i in range(n):  # Loop through n times
        print(a, end=' ')  # Print current Fibonacci number without a newline
        a, b = b, a + b  # Update a and b for the next Fibonacci numbers

# Call the fibonacci function with 10 as the argument
fibonacci(10)
