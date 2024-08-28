def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Input: Number of terms to generate
n = int(input("Enter the number of Fibonacci terms: "))

# Output: Fibonacci sequence
fib_sequence = fibonacci(n)
print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")
