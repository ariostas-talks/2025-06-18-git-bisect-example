def fib(n):
    if n < 0:
        raise ValueError("Input must be positive")

    a = 0
    b = 1

    # Check if n is equal to 0
    if n in (0, 1):
        return n
      
    for i in range(1, n):
        c = a + b
        a = b
        b = c

    return b

