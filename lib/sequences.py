#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print("[]")
    elif length == 1:
        print("[0]")
    else:
        a, b = 0, 1
        fib_sequence = [a]
        for _ in range(1, length):
            fib_sequence.append(b)
            a, b = b, a + b
        print(fib_sequence)