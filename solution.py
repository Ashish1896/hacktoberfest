# Hacktoberfest Contribution - Python Solution
# Author: Ashish1896
# Description: A simple Python program for Hacktoberfest

def fibonacci(n):
    """
    Generate fibonacci sequence up to n terms
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

def main():
    print("Welcome to Hacktoberfest 2025!")
    n = 10
    result = fibonacci(n)
    print(f"First {n} fibonacci numbers: {result}")
    
    # Calculate sum of even fibonacci numbers
    even_sum = sum(num for num in result if num % 2 == 0)
    print(f"Sum of even fibonacci numbers: {even_sum}")

if __name__ == "__main__":
    main()
