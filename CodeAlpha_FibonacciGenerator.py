def generate_fibonacci(n):
    fibonacci_seq = [0, 1]  # Initialize with the first two Fibonacci numbers
    for i in range(2, n):
        next_num = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_num)
    return fibonacci_seq

# Example: Generate the first 10 Fibonacci numbers
fibonacci_sequence = generate_fibonacci(10)
print(fibonacci_sequence)
